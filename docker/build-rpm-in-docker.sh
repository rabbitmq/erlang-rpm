#!/bin/sh
#
#
#
centos_version="$1"
build_dir="build-dir-$centos_version"
packages=( "Makefile" "*.patch" "erlang.spec" "Erlang_ASL2_LICENSE.txt" )
#
#
#
if [ -z $centos_version ]
then
	echo "
Ops: parameters error
first: version, ex: 6 or 7
-----------------------------------------
Ex: ./build-rpm-in-docker.sh 7
"
	exit 1
fi
#
#
#
if [ -e "$build_dir" ]
then
	sudo rm -rf "$build_dir"
	mkdir -p "$build_dir"
else
	mkdir "$build_dir"
fi
#
#
#
for file in "${packages[@]}"
do
	cp ../$file "$build_dir"
done
#
#
#
if [ -e ../dist ]
then
	cp -r ../dist "$build_dir"/dist
fi
#
#
#
sudo docker run -i -t -v ${PWD}/"$build_dir":/build/"$build_dir" erlang-rpm-build-"$centos_version"
