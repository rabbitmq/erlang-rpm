#!/usr/bin/env bash

os_name="$1"

# this has to match what Dockerfile uses
build_dir="pkg-build-dir"
pkg_files=("Makefile" "erlang.spec" "Erlang_ASL2_LICENSE.txt")

if [ -z "$os_name" ]
then
	echo "
Ops: parameters error
first: version or distribution name, ex: stream9, stream8, f38
-----------------------------------------
Ex: ./build-rpm-in-docker.sh stream9
Ex: ./build-rpm-in-docker.sh stream8
"
	exit 1
fi

echo "Re-creating build dir $build_dir"

if [ -e "$build_dir" ]
then
	rm -rf "$build_dir"
fi

mkdir "$build_dir"

echo "Copying patches to build dir $build_dir"
cp ../*.patch "$build_dir"

echo "Copying other files to build dir $build_dir"
for file in "${pkg_files[@]}"
do
	cp ../"$file" "$build_dir"
done

case $(uname -s) in
	Linux)
		sudo docker run -i -t --dns 8.8.8.8 -v "$PWD"/"$build_dir":/build/"$build_dir" "erlang-rpm-build-$os_name";;
	*)
		docker run -i -t --dns 8.8.8.8 -v "$PWD"/"$build_dir":/build/"$build_dir" "erlang-rpm-build-$os_name";;
esac
