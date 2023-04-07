#!/usr/bin/env sh

usage() {
  echo "parameters error"
	echo "first: version, e.g. 'stream9' or 'stream8' "
	echo "second: docker build arguments such as '--no-cache' [optional]"
	echo "./build-image-and-rpm.sh 'stream9' --no-cache"
  exit 1
}


if [ $# -lt 1 ]
then
  usage
fi

./build-docker-image.sh "$1" "$2"
./build-rpm-in-docker.sh "$1"
