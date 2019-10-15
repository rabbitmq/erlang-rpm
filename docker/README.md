# Docker Build Environment

This directory contains tooling that sets up a CentOS 8, 7, or 6
Docker image which can be used to build the RPM.

Run

``` bash
./build-docker-image.sh 8 --no-cache
```

to build a CentOS Docker image with all the build dependencies, then run

``` bash
./build-rpm-in-docker.sh 8
```

to do the build. This will create a directory `build-dir` in this
directory; you can later get the RPM out of there.

``` bash
./build-image-and-rpm.sh 8 --no-cache
```

to execute create the Docker image and build the RPM.

``` bash
./build-packages.sh
```

will produce three packages for CentOS versions from 6 to 8.
