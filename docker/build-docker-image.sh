#!/bin/sh
#
#
#
_dockerfile="Dockerfile"
_dockertemp="Dockerfile.template"
_parameter1="$1"
_parameter2="$2"
_dockerdir="docker-centos-$_parameter1"
#
#
#
if [ -z $_parameter1 ]
then
	echo "
Opps: parameters error
first: version, ex: 6 or 7
second: --no-cache [optional]
-----------------------------------------
Ex: ./build-docker-image.sh 7 --no-cache
Ex: ./build-docker-image.sh 7
Ex: ./build-docker-image.sh 6 --no-cache
EX: ./build-docker-image.sh 6
"
	exit 1
fi
#
#
#
if [ -e Dockerfile ]
then
	rm -f Dockerfile
fi
#
#
#
if [ -e "$_dockerdir" ]
then
	rm -rf "$_dockerdir"
	mkdir "$_dockerdir"
fi
#
#
#
if [ -e "$_dockertemp" ]
then
	cp Dockerfile.template  "$_dockerdir"/Dockerfile
	sed -i 's/{centosfrom}/'$1'/g' "$_dockerdir"/Dockerfile
	if [ -z $_parameter2 ]
	then
		sudo docker build -t="erlang-rpm-build-""$_parameter1" "$_dockerdir"
	else
		sudo docker build "$_parameter2" -t="erlang-rpm-build-""$_parameter1" "$_dockerdir"
	fi
fi
#
#
#
