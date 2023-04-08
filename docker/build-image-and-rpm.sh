#!/usr/bin/env sh

usage() {
	echo "
This script takes two arguments.
first: distribution, one of stream9, stream8, al2023, fedora, rocky, alma, oracle
second: docker build parameters such as --no-cache
-----------------------------------------
Ex: ./build-image-and-rpm.sh stream9 --no-cache
Ex: ./build-image-and-rpm.sh stream8 --no-cache
Ex: ./build-image-and-rpm.sh fedora38 --no-cache
"
  exit 1
}


if [ $# -lt 1 ]
then
  usage
fi

./build-docker-image.sh "$1" "$2"
./build-rpm-in-docker.sh "$1"
