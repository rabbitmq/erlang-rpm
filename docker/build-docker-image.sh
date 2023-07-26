#!/usr/bin/env sh

os_name="$1"
docker_params=${2:-"--pull"}
dockerfile="Dockerfile.template"

case $os_name in
	9|stream9|centos9)
		image="quay.io/centos/centos"
		image_tag=stream9;;
	8|stream8|centos8)
		image="quay.io/centos/centos"
		image_tag=stream8;;
	fedora|f38|fc38|fedora38)
		image="fedora"
		image_tag="38";;
	fedora|f39|fc39|fedora39)
		image="fedora"
		image_tag="39";;
	al|al2023|amazonlinux2023)
		image="amazonlinux"
		image_tag="2023";;
	oracle|oracle9|oraclelinux9)
		image="oraclelinux"
		image_tag="9";;
	rocky|rocky9|rockylinux9)
		image="rockylinux"
		image_tag="9";;
	alma|alma9|almalinux9)
		image="almalinux"
		image_tag="9";;
esac

docker_dir="docker-$os_name"

if [ -z "$os_name" ]
then
	echo "
This script takes two arguments.
first: distribution, one of stream9, stream8, al2023, fedora, rocky, alma, oracle
second: docker build parameters such as --no-cache
-----------------------------------------
Ex: ./build-docker-image.sh stream9 --no-cache
Ex: ./build-docker-image.sh stream8 --no-cache
Ex: ./build-docker-image.sh fedora38 --no-cache
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
			sudo docker build --build-arg image="$image" --build-arg image_tag="$image_tag" "$docker_params" -t="erlang-rpm-build-$os_name" "$docker_dir";;
		*)
			docker build --build-arg image="$image" --build-arg image_tag="$image_tag" "$docker_params" -t="erlang-rpm-build-$os_name" "$docker_dir";;
	esac