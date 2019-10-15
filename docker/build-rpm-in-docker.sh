#!/usr/bin/env bash

centos_version="$1"
build_dir="build-dir-$centos_version"
packages=("Makefile" "erlang.spec" "Erlang_ASL2_LICENSE.txt")

if [ -z "$centos_version" ]
then
	echo "
Ops: parameters error
first: version, ex: 8, 7, or 6
-----------------------------------------
Ex: ./build-rpm-in-docker.sh 8
Ex: ./build-rpm-in-docker.sh 7
"
	exit 1
fi

echo "Recreating build dir $build_dir"

if [ -e "$build_dir" ]
then
	rm -rf "$build_dir"
fi

mkdir "$build_dir"

echo "Copying patches to build dir $build_dir"
cp ../*.patch "$build_dir"

echo "Copying other files to build dir $build_dir"
for file in "${packages[@]}"
do
	cp ../"$file" "$build_dir"
done

if [ -e ../dist ]
then
	cp -r ../dist "$build_dir"/dist
fi

case $(uname -s) in
	Linux)
		sudo docker run -i -t -v "$PWD"/"$build_dir":/build/"$build_dir" erlang-rpm-build-"$centos_version";;
	*)
		docker run -i -t -v "$PWD"/"$build_dir":/build/"$build_dir" erlang-rpm-build-"$centos_version";;
esac
