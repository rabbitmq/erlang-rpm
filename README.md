# Zero-dependency Erlang RPM for RabbitMQ

This is a (virtually) zero dependency 64-bit Erlang RPM package that provides **just enough to run RabbitMQ**.
It may be easier to install than other Erlang RPMs in most environments.
It may or may not be suitable for running other Erlang-based software or 3rd party RabbitMQ
plugins.

This package has an **implicit OpenSSL/libcrypto dependency** (see below).

Team RabbitMQ also packages [recent Erlang/OTP releases for Debian](https://www.rabbitmq.com/install-debian.html#erlang-repositories).


## Provided Erlang/OTP Versions

The package targets Erlang/OTP `24.x` and `23.x`. Only 64-bit (x86-64) packages are provided.

### RabbitMQ Version Compatibility

See [Supported Erlang Versions](https://www.rabbitmq.com/which-erlang.html) in RabbitMQ documentation
for an up-to-date compatibility matrix.

#### Erlang 24

Erlang 24 is supported by RabbitMQ [starting with `3.8.16`](https://www.rabbitmq.com/changelog.html)
[as of May 2021](https://blog.rabbitmq.com/posts/2021/03/erlang-24-support-roadmap/).

It will also be supported by the next feature release, `3.9.0`.

#### Erlang 23

Erlang 23 is supported by RabbitMQ [starting with `3.8.4`](https://groups.google.com/forum/#!topic/rabbitmq-users/wlPIWz3UYHQ).

[RabbitMQ Erlang Version Requirements guide](https://www.rabbitmq.com/which-erlang.html) explains what Erlang/OTP
releases are supported by a given RabbitMQ release. We **highly recommend** following the recommendations
from that guide and using the most recent release in the supported series.


## Implicit OpenSSL/libcrypto Dependency

This package intentionally **does not include OpenSSL**/libcrypto. It must be provisioned separately.
Recent Erlang versions require a modern OpenSSL version, currently this means `1.1.x` or later.

## Supported RHEL, CentOS and Fedora Versions

Please note the **implicit OpenSSL/libcrypto dependency** section above.

 * RHEL or CentOS 8
 * RHEL or CentOS 7
 * Rocky Linux

The CentOS 8 version of the package usually works as expected on modern Fedora releases and Rocky Linux.

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

To use the most recent version on CentOS 8:

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

To use the most recent version on CentOS 7:

``` ini
# In /etc/yum.repos.d/rabbitmq_erlang.repo
[rabbitmq_erlang]
name=rabbitmq-rabbitmq-erlang
baseurl=https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/rpm/el/7/$basearch
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

[rabbitmq_erlang-noarch]
name=rabbitmq-rabbitmq-erlang-noarch
baseurl=https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/rpm/el/7/noarch
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

[rabbitmq_erlang-source]
name=rabbitmq-rabbitmq-erlang-source
baseurl=https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/rpm/el/7/SRPMS
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

Package Cloud supports a variety of options for RPM package installation: from Yum configuration to shell scripts
to Chef and Puppet.

See [Package Cloud repository installation](https://packagecloud.io/rabbitmq/erlang/install) page
for details.

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
       https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc
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
       https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
```

To install the package:

``` shell
yum install erlang
```

To use the most recent version on CentOS 7:

``` ini
# In /etc/yum.repos.d/rabbitmq_erlang.repo
[rabbitmq_erlang]
name=rabbitmq_erlang
baseurl=https://packagecloud.io/rabbitmq/erlang/el/7/$basearch
repo_gpgcheck=1
gpgcheck=1
enabled=1
# PackageCloud's repository key and RabbitMQ package signing key
gpgkey=https://packagecloud.io/rabbitmq/erlang/gpgkey
       https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300

[rabbitmq_erlang-source]
name=rabbitmq_erlang-source
baseurl=https://packagecloud.io/rabbitmq/erlang/el/7/SRPMS
repo_gpgcheck=1
gpgcheck=0
enabled=1
# PackageCloud's repository key and RabbitMQ package signing key
gpgkey=https://packagecloud.io/rabbitmq/erlang/gpgkey
       https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
```

To install the package:

``` shell
yum install erlang
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
 * hipe
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

```sh
cd docker

#
# Use build-image-and-rpm.sh to execute all scripts:
# build a Centos 8 image and build the RPM using it
#
./build-image-and-rpm.sh 8 --no-cache

#
# To only build a CentOS 8 Docker image with necessary toolchain
#
 ./build-docker-image.sh 8 --no-cache

#
# To only build the RPM using an already built and available image
#
./build-rpm-in-docker 8
```

then find the result under `docker/build-dir-{CentOSVersion}/RPMS/x86_64/`,
e.g. `build-dir-8/RPMS/x86_64/`.

For CentOS 7, replace the `8` in the examples above with a `7`.


### Without Docker

You must be running an RPM-based distro (CentOS 8, 7 or equivalent RHEL is highly recommended) for this to work.

``` shell
# add sudo if required by the local Docker installation
make
```

and see `RPMS/x86_64/`. Note that all artifacts created this way may be owned by root
due to the use of `sudo`.


### Patched Files

The patches applied affect the following files:

 * [erts/etc/common/Makefile.in](https://github.com/erlang/otp/commits/maint/erts/etc/common/Makefile.in)
 * [erts/etc/unix/Install.src](https://github.com/erlang/otp/commits/maint/erts/etc/unix/Install.src)
 * [erts/preloaded/src/Makefile](https://github.com/erlang/otp/commits/maint/erts/preloaded/src/Makefile)
 * [lib/asn1/c_src/Makefile](https://github.com/erlang/otp/commits/maint/lib/asn1/c_src/Makefile)
 * [lib/asn1/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/asn1/src/Makefile)
 * [lib/compiler/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/compiler/src/Makefile)
 * [lib/crypto/c_src/crypto.c](https://github.com/erlang/otp/blob/maint/lib/crypto/c_src/crypto.c)
 * [lib/crypto/c_src/Makefile.in](https://github.com/erlang/otp/commits/maint/lib/crypto/c_src/Makefile.in)
 * [lib/crypto/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/crypto/src/Makefile)
 * [lib/crypto/priv/Makefile](https://github.com/erlang/otp/commits/maint/lib/crypto/priv/Makefile)
 * [lib/debugger/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/debugger/src/Makefile)
 * [lib/edoc/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/edoc/src/Makefile)
 * [lib/erl_docgen/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/erl_docgen/src/Makefile)
 * [lib/erl_interface/src/Makefile.in](https://github.com/erlang/otp/commits/maint/lib/erl_interface/src/Makefile.in)
 * [lib/hipe/cerl/Makefile](https://github.com/erlang/otp/commits/maint/lib/hipe/cerl/Makefile)
 * [lib/hipe/flow/Makefile](https://github.com/erlang/otp/commits/maint/lib/hipe/flow/Makefile)
 * [lib/hipe/icode/Makefile](https://github.com/erlang/otp/commits/maint/lib/hipe/icode/Makefile)
 * [lib/hipe/main/Makefile](https://github.com/erlang/otp/commits/maint/lib/hipe/main/Makefile)
 * [lib/hipe/misc/Makefile](https://github.com/erlang/otp/commits/maint/lib/hipe/misc/Makefile)
 * [lib/hipe/rtl/Makefile](https://github.com/erlang/otp/commits/maint/lib/hipe/rtl/Makefile)
 * [lib/hipe/util/Makefile](https://github.com/erlang/otp/commits/maint/lib/hipe/util/Makefile)
 * [lib/inets/src/http_client/Makefile](https://github.com/erlang/otp/commits/maint/lib/inets/src/http_client/Makefile)
 * [lib/inets/src/http_lib/Makefile](https://github.com/erlang/otp/commits/maint/lib/inets/src/http_lib/Makefile)
 * [lib/inets/src/http_server/Makefile](https://github.com/erlang/otp/commits/maint/lib/inets/src/http_server/Makefile)
 * [lib/inets/src/inets_app/Makefile](https://github.com/erlang/otp/commits/maint/lib/inets/src/inets_app/Makefile)
 * [lib/kernel/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/kernel/src/Makefile)
 * [lib/mnesia/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/mnesia/src/Makefile)
 * [lib/os_mon/c_src/Makefile.in](https://github.com/erlang/otp/commits/maint/lib/os_mon/c_src/Makefile.in)
 * [lib/os_mon/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/os_mon/src/Makefile)
 * [lib/parsetools/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/parsetools/src/Makefile)
 * [lib/public_key/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/public_key/src/Makefile)
 * [lib/reltool/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/reltool/src/Makefile)
 * [lib/runtime_tools/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/runtime_tools/src/Makefile)
 * [lib/sasl/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/sasl/src/Makefile)
 * [lib/snmp/src/agent/Makefile](https://github.com/erlang/otp/commits/maint/lib/snmp/src/agent/Makefile)
 * [lib/snmp/src/app/Makefile](https://github.com/erlang/otp/commits/maint/lib/snmp/src/app/Makefile)
 * [lib/snmp/src/compile/Makefile](https://github.com/erlang/otp/commits/maint/lib/snmp/src/compile/Makefile)
 * [lib/snmp/src/manager/Makefile](https://github.com/erlang/otp/commits/maint/lib/snmp/src/manager/Makefile)
 * [lib/snmp/src/misc/Makefile](https://github.com/erlang/otp/commits/maint/lib/snmp/src/misc/Makefile)
 * [lib/ssl/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/ssl/src/Makefile)
 * [lib/stdlib/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/stdlib/src/Makefile)
 * [lib/syntax_tools/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/syntax_tools/src/Makefile)
 * [lib/tools/c_src/Makefile.in](https://github.com/erlang/otp/commits/maint/lib/tools/c_src/Makefile.in)
 * [lib/tools/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/tools/src/Makefile)
 * [lib/xmerl/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/xmerl/src/Makefile)


## Older Versions

The directory `versions` contains the patch files used for the older versions. Git repository
history can be useful as well.


## Copyright and License

Copyright VMware, Inc and its affiliates, 2011-2021. All Rights Reserved.

Released under the [Apache Software License 2.0](./Erlang_ASL2_LICENSE.txt),
same as Erlang/OTP starting with 18.0.
