#!/usr/bin/env bash
# Convenience: build the image for a flavor, then build the RPM in it.
set -euo pipefail

if [[ $# -lt 1 ]]; then
	echo "Usage: build-image-and-rpm.sh <flavor> [extra docker build args...]" >&2
	exit 1
fi

cd "$(dirname "$0")"
./build-docker-image.sh "$@"
./build-rpm-in-docker.sh "$1"
