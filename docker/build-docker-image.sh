#!/bin/sh
rm -f Dockerfile
DIR_DOCKER_FILE=docker-centos-$1
rm -rf $DIR_DOCKER_FILE
mkdir  $DIR_DOCKER_FILE
cp Dockerfile.template  $DIR_DOCKER_FILE/Dockerfile
sed -i 's/{centosfrom}/'$1'/g' $DIR_DOCKER_FILE/Dockerfile
sudo docker build $2 -t="erlang-rpm-build-"$1 $DIR_DOCKER_FILE 

