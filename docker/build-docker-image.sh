#!/usr/bin/env bash
# Build the OCI image used to produce the zero-dependency Erlang RPM
# for CentOS 7. CentOS 7 predates systemd and ships a low default
# nofile limit, so we raise it for the build (Erlang has a lot of
# files). Works with docker or podman; no sudo.

set -euo pipefail

# shellcheck source=common.sh
. "$(dirname "$0")/common.sh"

usage() {
	cat >&2 <<'EOF'
Usage: build-docker-image.sh <flavor> [extra build args...]

Flavors:
  7 | centos7   CentOS 7 (the only supported flavor on this branch)
EOF
	exit 1
}

[[ $# -ge 1 ]] || usage
flavor=$1; shift
extra_args=("$@")

case $flavor in
	7|centos7)
		image="quay.io/centos/centos"
		tag="centos7"
		dockerfile="Dockerfile.centos7.template"
		;;
	*)
		echo "Unknown flavor: $flavor" >&2
		echo "Use branch \`erlang-28\` for other variants, this branch for Erlang 28 is entirely CentOS 7-specific" >&2
		usage
		;;
esac

cd "$(dirname "$0")"

engine=$(detect_engine)
image_tag="erlang-rpm-build-$flavor"

echo "==> [$engine] Building image '$image_tag' from ${image}:${tag}"

# Stream the Dockerfile via stdin so the build has an empty context.
"$engine" build \
	--pull \
	--ulimit nofile=1024000:1024000 \
	--build-arg "image=$image" \
	--build-arg "image_tag=$tag" \
	-t "$image_tag" \
	${extra_args[@]+"${extra_args[@]}"} \
	- < "$dockerfile"
