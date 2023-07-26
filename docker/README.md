# Docker Build Environment

This directory contains tooling that sets up a CentOS 8, 7, or 6
Docker image which can be used to build the RPM.

Run

``` bash
./build-docker-image.sh stream9 --no-cache
```

to build a CentOS Docker image with all the build dependencies, then run

## Building the RPM

``` bash
# builds a RHEL 9 and CentOS Stream 9 flavor of the image
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
# builds an Amazon Linux 2023 flavor of the image
./build-rpm-in-docker.sh al2023
```

``` bash
# builds a Fedora 38 flavor of the image
./build-rpm-in-docker.sh fc38
```

``` bash
# builds a Rocky Linux 9 flavor of the image
./build-rpm-in-docker.sh rockylinux
```

``` bash
# builds an Alma Linux 9 flavor of the image
./build-rpm-in-docker.sh almalinux
```

``` bash
# builds an Oracle Linux 9 flavor of the image
./build-rpm-in-docker.sh oraclelinux
```

The commands assume that the image for the targeted distribution was built (see the earlier step).

## Building All Flavors

``` bash
./build-packages.sh
```

will produce a number of packages for the most popular distributions (in the RabbitMQ community):

 * RHEL 9 and CentOS Stream 9 (including Rocky Linux 9, Alma Linux 9, Oracle Linux 9)
 * RHEL 8 and CentOS Stream 8
 * Amazon Linux 2023
 * Fedora 38
