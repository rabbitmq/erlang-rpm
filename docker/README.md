# Docker Build Environment

This directory contains tooling that sets up a Docker image which can be used to build
several flavors (varieties) of the zero-dependency Erlang RPM.

Run

``` bash
# builds a Docker image for building the RHEL 9/CentOS Stream 9 version
# of the RPM
./build-docker-image.sh stream9 --no-cache
```

to build a RHEL 9/CentOS Stream 9 Docker image with all the build dependencies installed.

Having this image, we can proceed to building an actual zero-dependency Erlang RPM.

## Building the RPM

``` bash
# builds a RHEL 9 and CentOS Stream 9 flavor of the package
./build-rpm-in-docker.sh stream9
```

to do the build. This will create a directory `all_rpms` in this
directory; the built RPMs will be copied there.

## Building Different Image Flavors

It is possible to build the RPM on and for a number of RPM-based operating systems:

``` bash
# for RHEL 9 and CentOS Stream 9
./build-image-and-rpm.sh stream9 --no-cache
```

``` bash
# builds an Amazon Linux 2023 flavor of the package
./build-rpm-in-docker.sh al2023
```

``` bash
# builds a Fedora 38 flavor of the package
./build-rpm-in-docker.sh fc38
```

``` bash
# builds a Fedora 39 flavor of the package
./build-rpm-in-docker.sh fc39
```

``` bash
# builds a Rocky Linux 9 flavor of the package
./build-rpm-in-docker.sh rocky
```

``` bash
# builds an Alma Linux 9 flavor of the package
./build-rpm-in-docker.sh alma
```

``` bash
# builds an Oracle Linux 9 flavor of the package
./build-rpm-in-docker.sh oracle
```

The commands assume that the image for the targeted distribution was built (see the earlier step).

Built RPMs can be found under `./pkg-build-dir/RPMS/{architecture}`.

## Building All Flavors

``` bash
./build-packages.sh
```

will produce a number of packages for the most popular distributions (in the RabbitMQ community):

 * RHEL 9 and CentOS Stream 9 (including Rocky Linux 9, Alma Linux 9, Oracle Linux 9)
 * RHEL 8 and CentOS Stream 8
 * Amazon Linux 2023
 * Fedora 38

Built RPMs will be copied to the `./all_rpms` directory under `docker`.