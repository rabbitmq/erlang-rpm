# Docker Build Environment

This directory contains tooling that sets up a CentOS 8, 7, or 6
Docker image which can be used to build the RPM.

Run

``` sh
./build-docker-image.sh 8 -no-cache
```

to initially build the docker image, then run

``` sh
./build-rpm-in-docker.sh 8
```

to do the build. This will create a directory `build-dir` in this
directory; you can later get the RPM out of there.

```
./build-image-and-rpm.sh 8 -no-cache
```

to execute create the Docker image and build the RPM.
