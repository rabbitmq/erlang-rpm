# Instructions for AI Agents

This repository contains a [zero dependency Erlang RPM package](https://github.com/rabbitmq/erlang-rpm/),
produced and maintained by the RabbitMQ core team.

This RPM package strips off some Erlang/OTP parts that are not needed for RabbitMQ and removes
the documentation that is installed on the host.

## Repository Layout

 * `README.md` explains the goal of the project, where the dnf/yum/RPM repositories are hosted, and how
   this package is different from certain other Erlang RPM packages
 * `Makefile` is used to drive the build. It contains the package version to download and build
 * `erlang.spec` is the RPM spec file for building the package, including a change log section
 * `otp-*.patch` files are patches from the RabbitMQ team that strip some non-essential parts of Erlang/OTP
   and skip ddocumentation installation
 * `docker/*` contains various bits for building the package in containers (using Docker, Podman, and other OCI build tools)
 * `docker/Dockerfile.template` contains a `Dockerfile` template that's used to produce `Dockerfile`s for each supported package
   flavor

## Artifacts

This package can be built and used on a variety of RPM-based operating systems (distributions). The names of those
flavors are used in the Docker container name and resulting package filenames:

 * `9` (or `stream9`, or `centos9`) for RHEL 9.x, Rocky Linux 9.x, AlmaLinux 9.x, Oracle Linux 9.x
 * `8` (or `stream8`, or `centos8`) for RHEL 8.x, Rocky Linux 8.x, AlmaLinux 8.x, Oracle Linux 8.x
 * `al2023` for Amazon Linux 2023
 * `fc42` for Fedora 42, `fc41` for Fedora 41, `fc40` for Fedora 40, and so on

## Branches

This repository has one branch per supported Erlang/OTP series:

 * `erlang-28` for Erlang/OTP 28.x
 * `erlang-27` for Erlang/OTP 27.x
 * `erlang-26` for Erlang/OTP 26.x
 * `erlang-25` for Erlang/OTP 25.x

Erlang 28.x is the most recent series.

## Build Dependencies

This package's build infrastructure can be found under `docker`. It requires a Docker or Docker-compatible daemon
to be installed and running.

### Building OCI Images for a Specific Build Environment

`docker/build-docker-image.sh` is used to build the OCI for each supported flavor, for example:

```bash
# build an OCI image for building the package for the RHEL 9/CentOS Stream9/Rocky Linux 9/AlmaLinux 9/Oracle Linux 9 family
docker/build-docker-image.sh 9
```

```bash
# build an OCI image for building the package for the RHEL 8/CentOS Stream8/Rocky Linux 8/AlmaLinux 8/Oracle Linux 8 family
docker/build-docker-image.sh 8
```

```bash
# build an OCI image for building the package for Fedora 42
docker/build-docker-image.sh fc42

# build an OCI image for building the package for Fedora 41
docker/build-docker-image.sh fc41
```

```bash
# build an OCI image for Amazon Linux 2023
docker/build-docker-image.sh al2023
```

### Building a Package in Specific Build Environments

`docker/build-package.sh` is used to build the package for each supported flavor, for example:

```bash
# build the package for the RHEL 9/CentOS Stream9/Rocky Linux 9/AlmaLinux 9/Oracle Linux 9 family
docker/build-package.sh 9
```

```bash
# build the package for the RHEL 8/CentOS Stream8/Rocky Linux 8/AlmaLinux 8/Oracle Linux 8 family
docker/build-package.sh 8
```

```bash
# build the package for Fedora 42
docker/build-package.sh fc42

# build the package for Fedora 41
docker/build-package.sh fc41
```

```bash
# build the package for Amazon Linux 2023
docker/build-package.sh al2023
```

### Other Build Directories

 * `docker/pkg-build-dir` is a top-level directory used by `docker/build-package.sh`, `rpmbuild`, and other tools involved
 * `docker/all_rpms` stores the final build artifacts: the RPM files

## Build Infrastructure

The build infrastructure (GitHub Actions) that produces the artifacts using the templates and scripts under `docker`
are hosted in a separate repository, [`rabbitmq/erlang-packages`](https://github.com/rabbitmq/erlang-packages).

## Updating for New Releases

When asked to update the package for a new Erlang/OTP release to a specific version, or told
that a new Erlang/OTP release is available,

 * Determine what series a new release belongs to and switch to the corresponding branch.
   For example, `28.0.3` belongs to the `28` series and should be done on the `erlang-28` branch;
   `27.4.3.3` belongs to the Erlang `27` series and should be done on the `erlang-27` branch; and so on
 * Update the version in `Makefile`
 * Update the version (the `package_ver` and `upstream_ver` global variables) and the change log section in `erlang.spec`
 * Use commit `4571febb4b22a9f36cc302bcd46a1aaf08670433` as an example

## Backporting

When asked to backport a change, always use the `-x` branch with `git cherry-pick`.

## Committing Changes

When committing changes to the repository, never add yourself as an author, a co-author, or a committer.

Never push your changes unless explicitly asked to do so. Let a human review them and push.

## Metadata: Updating `AGENTS.md`, `GEMINI.md`, `CLAUDE.md`

When updating `AGENTS.md`, `GEMINI.md` and `CLAUDE.md`, treat `AGENTS.md` as the primary instructions file,
and `GEMINI.md`, `CLAUDE.md` as copies (technically, symlinks).

Treat the branch for the most recent series (covered above) as the source of truth.
