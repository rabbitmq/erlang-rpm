#!/usr/bin/env bash
# Build the zero-dependency Erlang RPM for CentOS 7. This branch is
# entirely CentOS 7-specific; use branch `erlang-28` for other variants.
# The OTP source tarball is downloaded once into ./tarballs and reused.

set -euo pipefail

cd "$(dirname "$0")"

flavors=(
	centos7
)

for flavor in "${flavors[@]}"; do
	echo
	echo "############################################################"
	echo "# Building flavor: $flavor"
	echo "############################################################"
	./build-image-and-rpm.sh "$flavor"
done

echo
echo "==> All RPMs available in $PWD/all_rpms"
