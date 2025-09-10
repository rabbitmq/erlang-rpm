# Instructions for AI Agents

This repository contains a [zero dependency Erlang RPM package](https://github.com/rabbitmq/erlang-rpm/),
produced and maintained by the RabbitMQ core team.

This RPM package strips off some Erlang/OTP parts that are not needed for RabbitMQ and removes
the documentation that is installed on the host.

## Repository Layout

 * `README.md` explains the goal of the project, where the dnf/yum/RPM repositories are hosted, and how
   this package is different from certain other Erlang RPM packages
 * `erlang.spec` is the RPM spec file for building the package, including a change log section
 * `otp-*.patch` files are patches from the RabbitMQ team that strip some non-essential parts of Erlang/OTP
   and skip ddocumentation installation
 * `docker/*` contains various bits for building the package in containers (using Docker, Podman, and other OCI build tools)
 * `docker/Dockerfile.template` contains a `Dockerfile` template that's used to produce `Dockerfile`s for each supported package
   flavor

## Artifacts

This package can be built and used on a variety of RPM-based operating systems (distributions). The names of those
flavors are used in the Docker container name and resulting package filenames:

 * `el9` for RHEL 9.x, Rocky Linux 9.x, AlmaLinux 9.x, Oracle Linux 9.x
 * `el8` for RHEL 8.x, Rocky Linux 8.x, AlmaLinux 8.x, Oracle Linux 8.x
 * `al2023` for Amazon Linux 2023
 * `fc42` for Fedora 42, `fc41` for Fedora 41, `fc40` for Fedora 40, and so on

## Branches

This repository has one branch per supported Erlang/OTP series:

 * `erlang-28` for Erlang/OTP 28.x
 * `erlang-27` for Erlang/OTP 27.x
 * `erlang-26` for Erlang/OTP 26.x
 * `erlang-25` for Erlang/OTP 25.x

## Build Infrastructure

The build infrastructure (GitHub Actions) that produces the artifacts using the templates and scripts under `docker`
are hosted in a separate repository, [`rabbitmq/erlang-packages`](https://github.com/rabbitmq/erlang-packages).
