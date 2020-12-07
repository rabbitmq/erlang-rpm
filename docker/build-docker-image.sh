#!/usr/bin/env sh

docker_file="Dockerfile"
docker_template="Dockerfile.template"
centos_version="$1"
docker_params="$2"
docker_dir="docker-centos-$centos_version"
#
#
#
if [ -z "$centos_version" ]
then
	echo "
Ops: parameters error
first: version, ex: 8, or 7
second: docker build parameters such as --no-cache
-----------------------------------------
Ex: ./build-docker-image.sh 8 --no-cache
Ex: ./build-docker-image.sh 7 --no-cache
"
exit 1
fi

if [ -e "$docker_file" ]
then
	rm -f "$docker_file"
fi

if [ -e "$docker_dir" ]
then
	rm -rf "$docker_dir"
fi

mkdir "$docker_dir"

echo "Will build an image for CentOS $centos_version using Docker file at $docker_dir/$docker_file"

if [ -e "$docker_template" ]
then
	cp "$docker_template" "$docker_dir"/"$docker_file"
	case $(uname -s) in
		Linux)
			sed --in-place=".bak" "s/{centosfrom}/$centos_version/g" "$docker_dir"/"$docker_file"
			sudo docker build "$docker_params" -t="erlang-rpm-build-""$centos_version" "$docker_dir";;
		*)
			sed -i ".bak" "s/{centosfrom}/$centos_version/g" "$docker_dir"/"$docker_file"
			docker build "$docker_params" -t="erlang-rpm-build-""$centos_version" "$docker_dir";;
	esac
fi
