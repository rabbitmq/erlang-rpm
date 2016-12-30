#!/bin/sh
#
#	
#
_docker_file="Dockerfile"
_docker_temp="Dockerfile.template"
_parameter1="$1"
_parameter2="$2"
_docker_dir="docker-centos-$_parameter1"
#
#
#
if [ -z $_parameter1 ]
then
	echo "
Ops: parameters error
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
if [ -e "$_docker_file" ]
then
	rm -f "$_docker_file"
fi
#
#
#
if [ -e "$_docker_dir" ]
then
	rm -rf "$_docker_dir"
	mkdir "$_docker_dir"
fi
#
#
#
if [ -e "$_docker_temp" ]
then
	cp "$_docker_temp" "$_docker_dir"/"$_docker_file"
	sed -i 's/{centosfrom}/'$1'/g' "$_docker_dir"/"$_docker_file"
	if [ -z $_parameter2 ]
	then
		sudo docker build -t="erlang-rpm-build-""$_parameter1" "$_docker_dir"
	else
		sudo docker build "$_parameter2" -t="erlang-rpm-build-""$_parameter1" "$_docker_dir"
	fi
fi
#
#
#
