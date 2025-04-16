#!/usr/bin/env sh

os_name="$1"
docker_params=${2:-"--pull"}

dockerfile="Dockerfile.template"

dockerfile="Dockerfile.centos7.template"
image="quay.io/centos/centos"
image_tag=centos7

docker_dir="docker-$os_name"

if [ -z "$os_name" ]
then
	echo "
This script takes two arguments.
first: distribution in this case is always 7,
second: docker build parameters such as --no-cache
-----------------------------------------
Ex: ./build-docker-image.sh 7 --no-cache
Ex: ./build-docker-image.sh 7 --no-cache
Ex: ./build-docker-image.sh 7 --no-cache
"
exit 1
fi

if [ -e "$docker_dir" ]
then
	rm -rf "$docker_dir"
fi

mkdir "$docker_dir"

echo "Will build an image for ${image}:${image_tag} using Docker file at $docker_dir/Dockerfile"

cp "$dockerfile" "$docker_dir/Dockerfile"
	case $(uname -s) in
		Linux)
			sudo docker build --ulimit nofile=1024000:1024000 --build-arg image="$image" --build-arg image_tag="$image_tag" "$docker_params" -t="erlang-rpm-build-$os_name" "$docker_dir";;
		*)
			docker build --ulimit nofile=1024000:1024000 --build-arg image="$image" --build-arg image_tag="$image_tag" "$docker_params" -t="erlang-rpm-build-$os_name" "$docker_dir";;
	esac
