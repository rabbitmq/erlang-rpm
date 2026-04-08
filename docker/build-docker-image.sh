#!/usr/bin/env bash
# Build the OCI image used to produce the zero-dependency Erlang RPM
# for one RPM-based distribution flavor. Works with docker or podman
# on macOS and on RPM-based Linux. No sudo.

set -euo pipefail

# shellcheck source=common.sh
. "$(dirname "$0")/common.sh"

usage() {
	cat >&2 <<'EOF'
Usage: build-docker-image.sh <flavor> [extra build args...]

Flavors: 10|stream10  9|stream9  8|stream8
         rocky10|rocky9|rocky8  alma10|alma9
         oracle10|oracle9  al2023  fc42|fc41
EOF
	exit 1
}

[[ $# -ge 1 ]] || usage
flavor=$1; shift
extra_args=("$@")

case $flavor in
	fedora|f42|fc42|fedora42)        image="fedora";                tag="42" ;;
	f41|fc41|fedora41)               image="fedora";                tag="41" ;;
	al|al2023|amazonlinux2023)       image="amazonlinux";           tag="2023" ;;
	oracle10|oraclelinux10)          image="oraclelinux";           tag="10" ;;
	oracle|oracle9|oraclelinux9)     image="oraclelinux";           tag="9" ;;
	rocky10|rockylinux10)            image="rockylinux/rockylinux"; tag="10" ;;
	rocky|rocky9|rockylinux9)        image="rockylinux/rockylinux"; tag="9" ;;
	rocky8|rockylinux8)              image="rockylinux/rockylinux"; tag="8" ;;
	alma10|almalinux10)              image="almalinux";             tag="10" ;;
	alma|alma9|almalinux9)           image="almalinux";             tag="9" ;;
	10|stream10|centos10)            image="quay.io/centos/centos"; tag="stream10" ;;
	9|stream9|centos9)               image="quay.io/centos/centos"; tag="stream9" ;;
	8|stream8|centos8)               image="rockylinux";            tag="8" ;;
	*) echo "Unknown flavor: $flavor" >&2; usage ;;
esac

cd "$(dirname "$0")"

engine=$(detect_engine)
image_tag="erlang-rpm-build-$flavor"

echo "==> [$engine] Building image '$image_tag' from ${image}:${tag}"

# Stream the Dockerfile via stdin so the build has an empty context
# (no tarballs, RPMs, or transient build dirs get sent to the daemon).
"$engine" build \
	--pull \
	--build-arg "image=$image" \
	--build-arg "image_tag=$tag" \
	-t "$image_tag" \
	${extra_args[@]+"${extra_args[@]}"} \
	- < Dockerfile.template
