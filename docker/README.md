# Docker Build Environment (CentOS 7)

This branch is **entirely CentOS 7-specific**. Use branch `erlang-28`
for builds targeting any other distribution. The CentOS 7 image
statically links OpenSSL 1.1.1 into the resulting Erlang RPM so it
works on a system whose default OpenSSL is the EOL 1.0.2 from 2013.

The scripts work on macOS (Docker Desktop, Podman, OrbStack, ...) and
on RPM-based Linux distributions with any Docker-compatible daemon.
No `sudo` required: configure your daemon for rootless use or add
your user to the appropriate group.

## Quick Start

``` bash
# Build the OCI image (downloads CentOS 7, builds OpenSSL 1.1.1
# statically inside it).
./build-docker-image.sh centos7

# Build the RPM inside it.
./build-rpm-in-docker.sh centos7
```

The two steps can also be chained:

``` bash
./build-image-and-rpm.sh centos7
```

Built RPMs are copied to `./all_rpms/<arch>/`.

## Tarball Cache

The upstream Erlang/OTP source tarball is downloaded **once** into
`./tarballs` and reused on every subsequent run. Delete the file
(or the directory) to force a re-download. The host script bind-mounts
the cached tarball into `/tmp/$tarball` inside the container so the
in-container `Makefile` fast-path picks it up without re-downloading.

## Transient Build Directories

Each invocation of `build-rpm-in-docker.sh` stages its inputs in a
fresh `pkg-build-dir.XXXXXX` directory and removes it on exit (even
on failure or interrupt).

## CentOS 7 nofile ulimit

CentOS 7 predates systemd's per-service file-descriptor handling and
ships a low default `nofile` limit. Erlang/OTP has a lot of files,
so both `docker build` and `docker run` are invoked with
`--ulimit nofile=1024000:1024000`.
