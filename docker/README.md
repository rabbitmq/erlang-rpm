# Docker Build Environment

This directory contains tooling that builds the zero-dependency
Erlang RPM inside an OCI image, for several RPM-based distributions.

The scripts work on macOS (Docker Desktop, Podman, OrbStack, ...) and
on RPM-based Linux distributions with any Docker-compatible daemon.
None of them require `sudo`: configure your daemon for rootless use,
or add your user to the appropriate group.

## Quick Start

``` bash
# Build the OCI image for RHEL/Rocky/Alma/Oracle 9.x
./build-docker-image.sh 9

# Build the RPM inside it
./build-rpm-in-docker.sh 9
```

The two steps can also be chained:

``` bash
./build-image-and-rpm.sh 9
```

Built RPMs are copied to `./all_rpms`.

## Supported Flavors

| Flavor                              | Distributions                                          |
|-------------------------------------|--------------------------------------------------------|
| `10` / `stream10` / `centos10`      | RHEL, Rocky, Alma, Oracle Linux 10.x                   |
| `9`  / `stream9`  / `centos9`       | RHEL, Rocky, Alma, Oracle Linux 9.x                    |
| `8`  / `stream8`  / `centos8`       | RHEL, Rocky, Alma, Oracle Linux 8.x                    |
| `rocky10` / `rocky9` / `rocky8`     | Rocky Linux                                            |
| `alma10`  / `alma9`                 | AlmaLinux                                              |
| `oracle10` / `oracle9`              | Oracle Linux                                           |
| `al2023`                            | Amazon Linux 2023                                      |
| `fc42` / `fc41`                     | Fedora                                                 |

## Building Every Flavor

``` bash
./build-packages.sh
```

builds the package for every flavor we ship today and drops the
results into `./all_rpms`.

## Tarball Cache

The upstream Erlang/OTP source tarball is downloaded **once** into
`./tarballs` and reused across every flavor and every subsequent run.
Delete the file (or the directory) to force a re-download.

## Transient Build Directories

Each invocation of `build-rpm-in-docker.sh` stages its inputs in a
fresh `pkg-build-dir.XXXXXX` directory and removes it on exit (even
on failure or interrupt). The container chowns the artifacts back to
the invoking host user before exiting, so cleanup never needs `sudo`.
