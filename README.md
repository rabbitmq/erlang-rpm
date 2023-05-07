# Zero-dependency Erlang RPM for RabbitMQ

This is a (virtually) zero dependency Erlang RPM package that provides **just enough to run RabbitMQ**.
It may or may not be suitable for running other Erlang-based software or 3rd party RabbitMQ
plugins.

x86-64 binaries are provided with every release, while aarch64 (ARM64)
binaries will be limited to new major and minor release, and patches when resources allow.

Binary packages can be produced on any host that can run Docker, including
aarch64 hosts. See the **Building from Source** section below.

## Supported RPM-based Distributions

[Binary builds](https://github.com/rabbitmq/erlang-rpm/releases) of this package target **modern RPM-based distributions**:

 * RHEL 8.4 or later
 * CentOS Stream 8
 * CentOS Stream 9
 * Rocky Linux 8.5 or later
 * Fedora 34 or later
 * Amazon Linux 2023
 * Oracle Linux 9
 * Alma Linux 9

## CentOS 7 and derivatives

[Team RabbitMQ stopped supporting CentOS 7](https://blog.rabbitmq.com/posts/2022/04/centos-7-support-discontinued/) in May 2022.

[Erlang 25.3.1](https://github.com/rabbitmq/erlang-rpm/releases/tag/v25.3.1) includes one-off CentOS 7 packages
statically linked against OpenSSL 1.1.x.

Regular CentOS 7 and Amazon Linux 2 builds were produced up to [Erlang 23.3.4.18](https://github.com/rabbitmq/erlang-rpm/releases/tag/v23.3.4.18).
They are dynamically linked against OpenSSL 1.0.


## Packages for Debian-based Distributions

Team RabbitMQ also packages [recent Erlang/OTP releases for Debian](https://www.rabbitmq.com/install-debian.html#erlang-repositories)
and [a modern Erlang PPA for Ubuntu](https://rabbitmq.com/install-debian.html#apt-launchpad-erlang).


## Provided Erlang/OTP Versions

The package targets Erlang/OTP `25.x` and `24.x`. Both x86-64 and aarch64 versions can be
build in containers.

**Important**: Erlang 26 introduce a number of breaking changes around networking and TLS.
Packages of Erlang 26 will be provided when Erlang 26 support ships in a GA RabbitMQ release.

### RabbitMQ Version Compatibility

See [Supported Erlang Versions](https://www.rabbitmq.com/which-erlang.html) in RabbitMQ documentation
for an up-to-date compatibility matrix.

#### Erlang 25

Erlang 25 is supported by RabbitMQ [starting with `3.10.0`](https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.10.0).

Erlang 25 depends on OpenSSL 1.1, which is **not available on CentOS 7**. Therefore Erlang 25 packages
are **only produced for modern Fedora, Rocky Linux, CentOS Stream, and Amazon Linux 2023**.


#### Erlang 24

Erlang 24 is supported by RabbitMQ [starting with `3.8.16`](https://www.rabbitmq.com/changelog.html).

Erlang 24 depends on OpenSSL 1.1, which is **not available on CentOS 7**. Therefore Erlang 24 packages
are **only produced for modern Fedora, Rocky Linux and CentOS Stream**.


## Implicit OpenSSL/libcrypto Dependency

This package intentionally **does not include OpenSSL**/libcrypto. It must be provisioned separately.
Recent Erlang versions require a modern OpenSSL version, currently this means `1.1.x` or later.

## Release Artifacts

For direct RPM package downloads, see [GitHub releases](https://github.com/rabbitmq/erlang-rpm/releases).

There are two dnf repositories that distributed this package:

 * [rabbitmq/erlang on PackageCloud](https://packagecloud.io/rabbitmq/erlang/)
 * [rabbitmq/rabbitmq-erlang on Cloudsmith.io](https://cloudsmith.io/~rabbitmq/repos/rabbitmq-erlang/setup/#repository-setup-yum)

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

To use the PackageCloud dnf repository, a [separate PackageCloud repository key](https://packagecloud.io/rabbitmq/erlang/gpgkey) must be imported:

``` shell
## primary RabbitMQ signing key
rpm --import https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc
## modern Erlang repository
rpm --import https://packagecloud.io/rabbitmq/erlang/gpgkey
```

## Direct Downloads from GitHub

This package is [distributed as a single RPM](https://github.com/rabbitmq/erlang-rpm/releases), which makes it convenient to
download and install using `dnf install -y /path/to/erlang.rpm`.

#### Erlang 25 on CentOS Stream 9, Amazon Linux 2023, modern Fedora (x86-64 and aarch)

Erlang 25 x86-64 and aarch64 releases can be provisioned on RHEL 9, CentOS Stream 9, Amazon Linux 2023,
and modern Fedora using a [direct download](https://github.com/rabbitmq/erlang-rpm/releases):

``` shell
# This is just an example that uses an aarch64 package for Amazon Linux 2023
cd /tmp/
curl -sfL -O https://github.com/rabbitmq/erlang-rpm/releases/download/v25.3/erlang-25.3-1.amzn2023.aarch64.rpm
sudo dnf install -y ./erlang-25.3-1.amzn2023.aarch64.rpm
```

### Latest Erlang Version from PackageCloud

This package is distributed via a [dnf repository on PackageCloud](https://packagecloud.io/rabbitmq/erlang).

PackageCloud provides a shell script for quick repository setup:

``` shell
# inspect the script running it in a sudo shell!
curl -s https://packagecloud.io/install/repositories/rabbitmq/erlang/script.rpm.sh | sudo bash
```

#### Erlang 25 on RHEL 9, CentOS Stream 9, modern Fedora, Rocky Linux

To use the most recent version on CentOS Stream 9, modern Fedora, Rocky Linux:

``` ini
# In /etc/yum.repos.d/rabbitmq_erlang.repo
[rabbitmq_erlang]
name=rabbitmq_erlang
baseurl=https://packagecloud.io/rabbitmq/erlang/el/9/$basearch
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
baseurl=https://packagecloud.io/rabbitmq/erlang/el/9/SRPMS
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
dnf install erlang
```

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
dnf install erlang
```

## Latest Erlang Version from a Cloudsmith Mirror

This package is distributed via a [dnf repository on Cloudsmith](https://cloudsmith.io/~rabbitmq/repos/rabbitmq-erlang/packages/).

Cloudsmith provides shell scripts for quick dnf repository setup.
See the [Cloudsmith repository installation](https://cloudsmith.io/~rabbitmq/repos/rabbitmq-erlang/setup/#repository-setup-yum) page
for details.

The repository is **subject to traffic quotas**. When the quota is reached, no package
installations will be possible for up to several days.

The examples below use a mirror of the Cloudsmith repo. All packages in it are
**signed with the same signing key**.

### Erlang 25 on RHEL 9, CentOS Stream 9, modern Fedora, Rocky Linux (x86-64)

Erlang 25 x86-64 releases can be provisioned on RHEL 9, CentOS Stream 9, Rocky Linux, and modern Fedora
using a dnf (yum) repository (a Cloudsmith mirror):

``` ini
# In /etc/yum.repos.d/modern_erlang.repo
[modern-erlang]
name=modern-erlang-el9
# uses a Cloudsmith mirror @ yum1.novemberain.com.
# Unlike Cloudsmith, it does not have traffic quotas
baseurl=https://yum1.novemberain.com/el/9/$basearch
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
name=modern-erlang-el9-noarch
# uses a Cloudsmith mirror @ yum1.novemberain.com.
# Unlike Cloudsmith, it does not have traffic quotas
baseurl=https://yum1.novemberain.com/el/9/noarch
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
name=modern-erlang-el9-source
# uses a Cloudsmith mirror @ yum1.novemberain.com.
# Unlike Cloudsmith, it does not have traffic quotas
baseurl=https://yum1.novemberain.com/el/9/SRPMS
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

### Erlang 25 on RHEL 8, CentOS Stream 8, modern Fedora, Rocky Linux (x86-64)

Erlang 25 x86-64 releases can be provisioned on RHEL 8, CentOS Stream 8, Rocky Linux, and modern Fedora
using a dnf (yum) repository (a Cloudsmith mirror):

``` ini
# In /etc/yum.repos.d/modern_erlang.repo
[modern-erlang]
name=modern-erlang-el8
# uses a Cloudsmith mirror @ yum1.novemberain.com.
# Unlike Cloudsmith, it does not have traffic quotas
baseurl=https://yum1.novemberain.com/el/8/$basearch
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
baseurl=https://yum1.novemberain.com/el/8/noarch
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
baseurl=https://yum1.novemberain.com/el/8/SRPMS
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
