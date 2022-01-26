#!/usr/bin/env sh

usage() {
  	echo "parameters error"
	echo "first: version, e.g. '9' or '8' "
	echo "second: --no-cache [optional]"
	echo "es: ./build-image-and-rpm.sh '8' --no-cache"
  exit 1
}


if [ $# -lt 1 ]
then
  usage
fi

./build-docker-image.sh "$1" "$2"
./build-rpm-in-docker.sh "$1"
