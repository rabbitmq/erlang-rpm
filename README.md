# Zero-dependency Erlang RPM for RabbitMQ

This is a (virtually) zero dependency Erlang RPM package that provides **just enough to run RabbitMQ**.
It may or may not be suitable for running other Erlang-based software or 3rd party RabbitMQ
plugins.

Team RabbitMQ provides x86-64 builds of the package for CentOS Stream 8 and 9.

ARM64 versions of the package **are not provided as binary builds**. If you'd like to contribute
ARM64 builds and support, [let us know](https://github.com/rabbitmq/erlang-rpm/discussions/108).

## Supported RPM-based Distributions

Binary builds of this package target **modern RHEL and CentOS versions** (RHEL/CentOS Stream 8+) as well as recent Fedora releases:

 * RHEL 8.4 or later
 * CentOS Stream 8
 * CentOS Stream 9
 * Rocky Linux 8.5 or later
 * Fedora 34 or later
 * Amazon Linux 2023 (x86-64)

## What about CentOS 7 and derivatives?

Older releases (up to [Erlang 23.3.4.11](https://github.com/rabbitmq/erlang-rpm/releases/tag/v23.3.4.11))
include builds for CentOS 7 and CentOS 7-based distributions (namely Amazon Linux 2), and OpenSSL 1.0.

This package has an **implicit OpenSSL/libcrypto dependency** (see below). Starting with Erlang 24,
the minimum required version is **an equivalent of OpenSSL is 1.1**, only provided by Fedora,
Rocky Linux, CentOS Stream 8 and CentOS Stream 9.

## What about Debian-based distributions?

Team RabbitMQ also packages [recent Erlang/OTP releases for Debian](https://www.rabbitmq.com/install-debian.html#erlang-repositories)
and [a modern Erlang PPA for Ubuntu](https://rabbitmq.com/install-debian.html#apt-launchpad-erlang).


## Provided Erlang/OTP Versions

The package targets Erlang/OTP `25.x` and `24.x`. Only 64-bit (x86-64) packages are provided.

### RabbitMQ Version Compatibility

See [Supported Erlang Versions](https://www.rabbitmq.com/which-erlang.html) in RabbitMQ documentation
for an up-to-date compatibility matrix.

#### Erlang 25

Erlang 25 is supported by RabbitMQ [starting with `3.10.0`](https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.10.0).

Erlang 25 depends on OpenSSL 1.1, which is **not available on CentOS 7**. Therefore Erlang 25 packages
are **only produced for modern Fedora, Rocky Linux and CentOS Stream**.


#### Erlang 24

Erlang 24 is supported by RabbitMQ [starting with `3.8.16`](https://www.rabbitmq.com/changelog.html).

Erlang 24 depends on OpenSSL 1.1, which is **not available on CentOS 7**. Therefore Erlang 24 packages
are **only produced for modern Fedora, Rocky Linux and CentOS Stream**.


## Implicit OpenSSL/libcrypto Dependency

This package intentionally **does not include OpenSSL**/libcrypto. It must be provisioned separately.
Recent Erlang versions require a modern OpenSSL version, currently this means `1.1.x` or later.

## Supported RHEL, CentOS and Fedora Versions

Please note the **implicit OpenSSL/libcrypto dependency** section above.

 * For Erlang 25: supports RHEL or CentOS Stream 9 or CentOS Stream 8, modern Fedora, Rocky Linux. **Requires OpenSSL 1.1**
 * for Erlang 24: same as Erlang 25.


## Release Artifacts

For direct RPM package downloads, see [GitHub releases](https://github.com/rabbitmq/erlang-rpm/releases).

There are two Yum repositories that distributed this package:

 * [rabbitmq/rabbitmq-erlang on Cloudsmith.io](https://cloudsmith.io/~rabbitmq/repos/rabbitmq-erlang/setup/#repository-setup-yum)
 * [rabbitmq/erlang on Package Cloud](https://packagecloud.io/rabbitmq/erlang/)

See the repository setup instructions below.

### Signing Keys

The package is signed using the standard [RabbitMQ signing key](https://www.rabbitmq.com/signatures.html):

``` shell
## primary RabbitMQ signing key
rpm --import https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc
```

To use the Cloudsmith Yum repository, a [separate Cloudsmith repository key](https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/gpg.E495BB49CC4BBE5B.key) must be imported:

``` shell
## primary RabbitMQ signing key
rpm --import https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc
## modern Erlang repository
rpm --import 'https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/gpg.E495BB49CC4BBE5B.key'
```

To use the PackageCloud Yum repository, a [separate PackageCloud repository key](https://packagecloud.io/rabbitmq/erlang/gpgkey) must be imported:

``` shell
## primary RabbitMQ signing key
rpm --import https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc
## modern Erlang repository
rpm --import https://packagecloud.io/rabbitmq/erlang/gpgkey
```

### Latest Erlang Version from Cloudsmith

Cloudsmith provides shell scripts for quick Yum repository setup.
See the [Cloudsmith repository installation](https://cloudsmith.io/~rabbitmq/repos/rabbitmq-erlang/setup/#repository-setup-yum) page
for details.

#### Erlang 25 on RHEL 8, CentOS 8, modern Fedora, Rocky Linux

To use the most recent Erlang version on CentOS 8:

``` ini
# In /etc/yum.repos.d/rabbitmq_erlang.repo
[rabbitmq-rabbitmq-erlang]
name=rabbitmq-rabbitmq-erlang
baseurl=https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/rpm/el/8/$basearch
repo_gpgcheck=1
enabled=1
gpgkey=https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/gpg.E495BB49CC4BBE5B.key
gpgcheck=1
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
pkg_gpgcheck=1
autorefresh=1
type=rpm-md

[rabbitmq-rabbitmq-erlang-noarch]
name=rabbitmq-rabbitmq-erlang-noarch
baseurl=https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/rpm/el/8/noarch
repo_gpgcheck=1
enabled=1
gpgkey=https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/gpg.E495BB49CC4BBE5B.key
       https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc
gpgcheck=1
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
pkg_gpgcheck=1
autorefresh=1
type=rpm-md

[rabbitmq-rabbitmq-erlang-source]
name=rabbitmq-rabbitmq-erlang-source
baseurl=https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/rpm/el/8/SRPMS
repo_gpgcheck=1
enabled=1
gpgkey=https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/gpg.E495BB49CC4BBE5B.key
       https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc
gpgcheck=1
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
pkg_gpgcheck=1
autorefresh=1
type=rpm-md
```

To install the package:

``` shell
yum update -y
yum install -y erlang
```


### Latest Erlang Version from PackageCloud

#### Erlang 25 on RHEL 8, CentOS 8, modern Fedora, Rocky Linux

To use the most recent version on CentOS 8:

``` ini
# In /etc/yum.repos.d/rabbitmq_erlang.repo
[rabbitmq_erlang]
name=rabbitmq_erlang
baseurl=https://packagecloud.io/rabbitmq/erlang/el/8/$basearch
repo_gpgcheck=1
gpgcheck=1
enabled=1
# PackageCloud's repository key and RabbitMQ package signing key
gpgkey=https://packagecloud.io/rabbitmq/erlang/gpgkey
       https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300

[rabbitmq_erlang-source]
name=rabbitmq_erlang-source
baseurl=https://packagecloud.io/rabbitmq/erlang/el/8/SRPMS
repo_gpgcheck=1
gpgcheck=0
enabled=1
# PackageCloud's repository key and RabbitMQ package signing key
gpgkey=https://packagecloud.io/rabbitmq/erlang/gpgkey
       https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
```

To install the package:

``` shell
yum install erlang
```

Note that Erlang 25 packages **implicitly depend on OpenSSL 1.1** which is no available
on RHEL 7 or CentOS 7. Therefore Erlang 25 packages will fail to install
on those distributions.


## Available Erlang Applications

This package removes certain Erlang/OTP components that are non-essential
for running RabbitMQ but can greatly complicate installation process by bringing
in complicated dependencies.

Only the following OTP applications are provided:

 * asn1
 * compiler
 * crypto
 * eldap
 * erl_interface
 * erts
 * inets
 * kernel
 * mnesia
 * os_mon
 * public_key
 * reltool
 * runtime_tools
 * sasl
 * snmp
 * ssl
 * stdlib
 * syntax_tools
 * xmerl


## Building from Source

### With Docker

This repository provides scripts that can build an image with the `rpmbuild` toolchain
and build the package in it. They can be found under the `./docker` directory.

```sh
cd docker

#
# Use build-image-and-rpm.sh to execute all scripts:
# build an image and build the RPM in it
#
# Supported distribution aliases:
#  * stream9 for CentOS Stream 9
#  * stream8 for CentOS Stream 8
#  * al2023 for Amazon Linux 2023
#  * f38 for Fedora 38
#
./build-image-and-rpm.sh stream9 --no-cache

#
# To only build an image with the necessary toolchain,
# use ./build-docker-image.sh.
#
# Supported distribution aliases:
#  * stream9 for CentOS Stream 9
#  * stream8 for CentOS Stream 8
#  * al2023 for Amazon Linux 2023
#  * f38 for Fedora 38
 ./build-docker-image.sh stream9 --no-cache

#
# To only build the RPM using an already built and available image,
# use ./build-rpm-in-docker.sh
#
# Supported distribution aliases:
#  * stream9 for CentOS Stream 9
#  * stream8 for CentOS Stream 8
#  * al2023 for Amazon Linux 2023
#  * f38 for Fedora 38
#
./build-rpm-in-docker.sh stream9
```

Built packages can be found under `docker/pkg-build-dir/RPMS/{architecture}/`.

### Without Docker

On an RPM-based distro (CentOS Stream 9, modern Fedora or Amazon Linux 2023), the package can
be built without containers.

``` shell
# add sudo if necessary
make
```

and see `RPMS/{architecture}/`. Note that all artifacts created this way may be owned by root
due to the use of `sudo`.

### Scope of Patching

The patches apply to the build system only (Makefile, Makefile.in and similar files).
No source code is patched.


## Older Versions

The directory `versions` contains the patch files used for the older versions. Git repository
history and release archive can be useful as well.


## Copyright and License

Copyright VMware, Inc and its affiliates, 2011-2023. All Rights Reserved.

Released under the [Apache Software License 2.0](./Erlang_ASL2_LICENSE.txt),
same as Erlang/OTP starting with 18.0.
