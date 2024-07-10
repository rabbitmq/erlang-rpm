# Zero-dependency Erlang RPM for RabbitMQ

This is a (virtually) zero dependency Erlang RPM package that provides **just enough to run RabbitMQ**.
It may or may not be suitable for running other Erlang-based software or 3rd party RabbitMQ
plugins.

x86-64 binaries are provided with every release, while aarch64 (ARM64)
binaries will be limited to new major and minor release, and patches when resources allow.

Binary packages can be produced on any host that can run Docker, including
aarch64 hosts. See the **Building from Source** section below.

## Supported RPM-based Distributions

[Binary builds](https://github.com/rabbitmq/erlang-rpm/releases) of this package **target modern RPM-based distributions**:

 * RHEL 8.8 and later (the versions [covered by full support](https://access.redhat.com/support/policy/updates/errata))
 * CentOS Stream 9
 * Fedora 39  or later
 * Rocky Linux 8.10 and 9.4 (the [most recent maintained](https://wiki.rockylinux.org/rocky/version/) 8.x and 9.x series)
 * Alma Linux 8.10 and 9.4 (the [most recent maintained](https://wiki.almalinux.org/release-notes/) 8.x and 9.x series)
 * Amazon Linux 2023
 * Oracle Linux 9

## CentOS 8 has Reached End-of-Life

CentOS Stream 8 has [reached end of life](https://endoflife.date/centos-stream) in May 2024. The CentOS 8 versions
of these packages are produced on Rocky Linux 8.10+ from July 2024 and onwards.

## CentOS 7 has Reached End-of-Life

[Team RabbitMQ stopped supporting CentOS 7](https://blog.rabbitmq.com/posts/2022/04/centos-7-support-discontinued/) in May 2022.

Erlang [26.1](https://github.com/rabbitmq/erlang-rpm/releases/tag/v26.1) and [25.3.2.3](https://github.com/rabbitmq/erlang-rpm/releases/tag/v25.3.2.3)
include one-off CentOS 7 packages statically linked against OpenSSL 1.1.x.

Regular CentOS 7 and Amazon Linux 2 builds were produced up to [Erlang 23.3.4.18](https://github.com/rabbitmq/erlang-rpm/releases/tag/v23.3.4.18).
They are dynamically linked against OpenSSL 1.0.


## Packages for Debian-based Distributions

Team RabbitMQ also packages [recent Erlang/OTP releases for Debian](https://www.rabbitmq.com/install-debian.html#erlang-repositories)
and [a modern Erlang PPA for Ubuntu](https://rabbitmq.com/install-debian.html#apt-launchpad-erlang).


## Provided Erlang/OTP Versions

he package targets Erlang/OTP `26.x` and `25.x`. Both x86-64 and aarch64 versions can be
build in containers.

First RabbitMQ release series with Erlang 26 support is [`3.12`](https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.12.0).

### RabbitMQ Version Compatibility

See [Supported Erlang Versions](https://www.rabbitmq.com/which-erlang.html) in RabbitMQ documentation
for an up-to-date compatibility matrix.

#### Erlang 26

First RabbitMQ release series with Erlang 26 support is [`3.12`](https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.12.0).

#### Erlang 25

Erlang 25 is supported by RabbitMQ [starting with `3.10.0`](https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.10.0).

Erlang 25 depends on OpenSSL 1.1, which is **not available on CentOS 7**. Therefore Erlang 25 packages
are **only produced for modern Fedora, Rocky Linux, CentOS Stream, and Amazon Linux 2023**.


## Implicit OpenSSL/libcrypto Dependency

This package intentionally **does not include OpenSSL**/libcrypto. It must be provisioned separately.
Recent Erlang versions require a modern OpenSSL version, currently this means `1.1.x` or later.

## Release Artifacts

For direct RPM package downloads, see [GitHub releases](https://github.com/rabbitmq/erlang-rpm/releases).

There is also a dnf repository that distributes x64_86 builds of this package.
See the repository setup instructions below.

### Signing Keys

The package is signed using the standard [RabbitMQ signing key](https://www.rabbitmq.com/signatures.html):

``` shell
## primary RabbitMQ signing key
rpm --import https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc
```

To use the Cloudsmith dnf repository, a [separate Cloudsmith repository key](https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/gpg.E495BB49CC4BBE5B.key) must be imported:

``` shell
## primary RabbitMQ signing key
rpm --import https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc
## modern Erlang repository
rpm --import 'https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/gpg.E495BB49CC4BBE5B.key'
```

## Direct Downloads from GitHub

This package is [distributed as a single RPM](https://github.com/rabbitmq/erlang-rpm/releases), which makes it convenient to
download and install using `dnf install -y /path/to/erlang.rpm`.

Erlang 25 x86-64 and aarch64 releases can be provisioned on RHEL 9, CentOS Stream 9, Amazon Linux 2023,
and modern Fedora using a [direct download](https://github.com/rabbitmq/erlang-rpm/releases):

``` shell
# This is just an example that uses an aarch64 package for Amazon Linux 2023
cd /tmp/
curl -sfL -O https://github.com/rabbitmq/erlang-rpm/releases/download/v25.3.2.5/erlang-25.3.2.5-1.amzn2023.aarch64.rpm
sudo dnf install -y ./erlang-25.3.2.5-1.amzn2023.aarch64.rpm
```

## Latest Erlang Version from a Cloudsmith Mirror

This package is distributed via a dnf repository that mirrors from Cloudsmith.

The upstream Cloudsmith repository is **subject to traffic quotas**. When the quota is reached, package
installations will only be possible from the mirrors, so it is highly recommended that you use them.

The examples below use a mirror of the Cloudsmith repo. All packages in it are
**signed with the same signing key**.

### Erlang 25 on RHEL 9, CentOS Stream 9, modern Fedora, Rocky Linux 9 (x86-64)

Erlang 25 x86-64 releases can be provisioned on RHEL 9, CentOS Stream 9, Rocky Linux, and modern Fedora
using a dnf (yum) repository (a Cloudsmith mirror):

``` ini
# In /etc/yum.repos.d/modern_erlang.repo

##
## Zero dependency Erlang RPM
##

[modern-erlang]
name=modern-erlang-el8
# uses a Cloudsmith mirror @ yum.novemberain.com in addition to its Cloudsmith upstream.
# Unlike Cloudsmith, the mirror does not have any traffic quotas
baseurl=https://yum1.novemberain.com/erlang/el/8/$basearch
        https://yum2.novemberain.com/erlang/el/8/$basearch
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

[modern-erlang-noarch]
name=modern-erlang-el8-noarch
# uses a Cloudsmith mirror @ yum.novemberain.com.
# Unlike Cloudsmith, it does not have any traffic quotas
baseurl=https://yum1.novemberain.com/erlang/el/8/noarch
        https://yum2.novemberain.com/erlang/el/8/noarch
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

[modern-erlang-source]
name=modern-erlang-el8-source
# uses a Cloudsmith mirror @ yum.novemberain.com.
# Unlike Cloudsmith, it does not have any traffic quotas
baseurl=https://yum1.novemberain.com/erlang/el/8/SRPMS
        https://yum2.novemberain.com/erlang/el/8/SRPMS
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
```

To install the package:

``` shell
dnf update -y
dnf install -y erlang
```

### Erlang 25 on RHEL 8, CentOS Stream 8, Rocky Linux 8 (x86-64)

Erlang 25 x86-64 releases can be provisioned on RHEL 8, CentOS Stream 8, Rocky Linux, and modern Fedora
using a dnf (yum) repository (a Cloudsmith mirror):

``` ini
# In /etc/yum.repos.d/modern_erlang.repo
[modern-erlang]
name=modern-erlang-el8
# uses a Cloudsmith mirror @ yum1.novemberain.com.
# Unlike Cloudsmith, it does not have traffic quotas
baseurl=https://yum1.novemberain.com/erlang/el/8/$basearch
        https://yum1.novemberain.com/erlang/el/8/$basearch
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

[modern-erlang-noarch]
name=modern-erlang-el8-noarch
# uses a Cloudsmith mirror @ yum1.novemberain.com.
# Unlike Cloudsmith, it does not have traffic quotas
baseurl=https://yum1.novemberain.com/erlang/el/8/noarch
        https://yum2.novemberain.com/erlang/el/8/noarch
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

[modern-erlang-source]
name=modern-erlang-el8-source
# uses a Cloudsmith mirror @ yum1.novemberain.com.
# Unlike Cloudsmith, it does not have traffic quotas
baseurl=https://yum1.novemberain.com/erlang/el/8/SRPMS
        https://yum2.novemberain.com/erlang/el/8/SRPMS
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
```

To install the package:

``` shell
dnf update -y
dnf install -y erlang
```

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

The recommended host environment for these builds is Fedora 38+. Due to Docker-specific volume
sharing permissions intricacies, performing such builds on macOS will require
modifications to the build scripts.

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
# Note: this will use sudo to drive `dnf update -y` and install a few packages
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
