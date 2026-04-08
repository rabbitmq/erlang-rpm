#!/usr/bin/env bash
# Build the zero-dependency Erlang RPM for every shipped flavor.
# The OTP source tarball is downloaded once and reused across flavors.

set -euo pipefail

cd "$(dirname "$0")"

flavors=(
	rocky10
	rocky9
	rocky8
	al2023
	fedora42
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
