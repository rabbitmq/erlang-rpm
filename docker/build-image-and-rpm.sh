#!/usr/bin/env sh

usage() {
  	echo "parameters error"
	echo "first: version, es: 6 or 7.1.1503 "
	echo "second: --no-cache [optional]"
	echo "es: ./build-image-and-rpm.sh 7.1.1503 --no-cache"
  exit 1
}


if [ $# -lt 1 ]
then
  usage
fi

./build-docker-image.sh "$1" "$2"
./build-rpm-in-docker "$1"
