#!/bin/sh
cd $(dirname $0)
mkdir -p build-dir-$1
cp ../* build-dir-$1
cp -r ../dist build-dir-$1/dist
sudo docker run -i -t -v ${PWD}/build-dir-$1:/build/build-dir-$1 erlang-rpm-build-$1
