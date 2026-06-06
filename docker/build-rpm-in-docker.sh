#!/usr/bin/env bash
# Build the zero-dependency Erlang RPM inside the OCI image produced
# by build-docker-image.sh. Reuses a shared upstream tarball cache
# (./tarballs) across all flavors and runs.

set -euo pipefail

# shellcheck source=common.sh
. "$(dirname "$0")/common.sh"

usage() {
	cat >&2 <<'EOF'
Usage: build-rpm-in-docker.sh <flavor>

Builds the package inside the 'erlang-rpm-build-<flavor>' image
previously produced by build-docker-image.sh.
EOF
	exit 1
}

[[ $# -ge 1 ]] || usage
flavor=$1

cd "$(dirname "$0")"
script_dir=$PWD
repo_root=$(cd .. && pwd)
engine=$(detect_engine)
image_tag="erlang-rpm-build-$flavor"

# Discover OTP version from the top-level Makefile.
otp_release=$(awk -F= \
	'/^OTP_RELEASE[[:space:]]*=/ { gsub(/[[:space:]]/, "", $2); print $2; exit }' \
	"$repo_root/Makefile")
[[ -n $otp_release ]] || { echo "Could not read OTP_RELEASE from Makefile" >&2; exit 1; }

tarball="OTP-${otp_release}.tar.gz"
url="https://github.com/erlang/otp/archive/${tarball}"

# Shared cache; one download per OTP version, regardless of flavor.
cache_dir="$script_dir/tarballs"
mkdir -p "$cache_dir"

if [[ ! -f "$cache_dir/$tarball" ]]; then
	echo "==> Downloading $tarball"
	tmp=$(mktemp "$cache_dir/.${tarball}.XXXXXX")
	trap 'rm -f "$tmp"' EXIT
	if command -v curl >/dev/null 2>&1; then
		curl -fL --retry 3 --output "$tmp" "$url"
	else
		wget -O "$tmp" "$url"
	fi
	mv "$tmp" "$cache_dir/$tarball"
	trap - EXIT
else
	echo "==> Reusing cached $cache_dir/$tarball"
fi

# Per-build transient directory; cleaned up on every exit path.
build_dir=$(mktemp -d "$script_dir/pkg-build-dir.XXXXXX")
cleanup() {
	# Fast path: remove as the host user.
	rm -rf "$build_dir" 2>/dev/null && return
	# Fallback: files inside may be owned by container root (rootful
	# docker on Linux), so ask a throwaway container to nuke them.
	"$engine" run --rm --pull=never \
		-v "$build_dir:/cleanup:z" \
		--entrypoint /bin/sh \
		"$image_tag" \
		-c 'find /cleanup -mindepth 1 -delete' >/dev/null 2>&1 || true
	rmdir "$build_dir" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

mkdir -p "$build_dir/tarballs" "$build_dir/dist"

# Stage a fresh copy of the cached tarball; the in-container Makefile
# may delete its working copy, but the shared cache stays intact.
cp -p "$cache_dir/$tarball" "$build_dir/tarballs/"

cp -p "$repo_root"/Makefile \
      "$repo_root"/erlang.spec \
      "$repo_root"/Erlang_ASL2_LICENSE.txt \
      "$build_dir/"
cp -p "$repo_root"/*.patch "$build_dir/"

echo "==> [$engine] Building RPM in $build_dir using image '$image_tag'"
# DNF_CMD override: '--nobest' keeps 'dnf update' from failing when a
# distribution is mid-point-release and its BaseOS/AppStream mirrors are
# temporarily out of sync (e.g. AppStream already serves N.M+1 builds
# whose dependencies BaseOS does not provide yet).
"$engine" run --rm \
	--pull=never \
	-v "$build_dir:/build/pkg-build-dir:z" \
	"$image_tag" \
	make "DNF_CMD=dnf --nobest"

# Collect every produced .rpm into all_rpms/<arch>/. The arch is the
# component just before the final ".rpm" suffix in the filename.
out_dir="$script_dir/all_rpms"
mkdir -p "$out_dir"
found=0
while IFS= read -r -d '' rpm; do
	base=$(basename "$rpm")
	stem=${base%.rpm}
	arch=${stem##*.}
	[[ -n $arch ]] || arch="unknown"
	mkdir -p "$out_dir/$arch"
	cp -p "$rpm" "$out_dir/$arch/"
	chmod 0644 "$out_dir/$arch/$(basename "$rpm")"
	found=$((found + 1))
done < <(find "$build_dir" -type f -name '*.rpm' -print0 2>/dev/null)

if (( found == 0 )); then
	echo "No RPMs were produced; build likely failed." >&2
	exit 1
fi

echo "==> $found RPM(s) copied to $out_dir"
