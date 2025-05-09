#!/usr/bin/env sh

usage() {
	echo "
This script takes two arguments.
first: distribution, one of rocky9, alma9, rocky8, al2023, fedora, oracle
second: docker build parameters such as --no-cache
-----------------------------------------
Ex: ./build-image-and-rpm.sh rocky9 --no-cache
Ex: ./build-image-and-rpm.sh rocky9 --no-cache
Ex: ./build-image-and-rpm.sh fedora41 --no-cache
"
  exit 1
}


if [ $# -lt 1 ]
then
  usage
fi

./build-docker-image.sh "$1" "$2"
./build-rpm-in-docker.sh "$1"
