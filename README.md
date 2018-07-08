# Zero-dependency Erlang RPM for RabbitMQ

This is a (virtually) zero dependency 64-bit Erlang RPM package that provides just enough to run RabbitMQ.
It may be easier to install than RPMs provided by Erlang Solutions in certain environments.
It may or may not be suitable for running other Erlang-based software or 3rd party RabbitMQ
plugins.

This package has an **implicit OpenSSL/libcrypto dependency** (see below).

## Provided Erlang/OTP Versions

The package currently targets Erlang/OTP `21.0.x`, `20.3.x`, `19.3.x`. Only 64-bit packages are provided.

Earlier releases going all the way to `18.3.x` are also available but get not updates unless
they address a critically important issue.

## Implicit OpenSSL/libcrypto Dependency

This package intentionally does not include OpenSSL/libcrypto. It must be provisioned separately.
Recent Erlang versions require a modern OpenSSL version, e.g. `1.0.1`.

## Supported CentOS Versions

Please note the **implicit OpenSSL/libcrypto dependency** section above.

 * CentOS 7
 * CentOS 6

## Release Artifacts

Yum repositories are available from [Bintray](https://bintray.com/rabbitmq/rpm/erlang) and [Package Cloud](https://packagecloud.io/rabbitmq/erlang/) (see repository setup instructions below).

RPM packages can be downloaded [from Bintray](https://bintray.com/rabbitmq/rpm/erlang) and [GitHub](https://github.com/rabbitmq/erlang-rpm/releases).

### Bintray Yum Repositories

To use the Bintray Yum repositories, here are the `.repo` configuration files:

#### Erlang 21.x

Note that [Erlang/OTP 21 is supported by RabbitMQ starting with version 3.7.7](https://github.com/rabbitmq/rabbitmq-server/releases/tag/v3.7.7).

To use Erlang 21.x on CentOS 7:

```ini
# In /etc/yum.repos.d/rabbitmq-erlang.repo
[rabbitmq-erlang]
name=rabbitmq-erlang
baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/21/el/7
gpgcheck=1
gpgkey=https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc
repo_gpgcheck=0
enabled=1
```

To use Erlang 21.x on CentOS 6:

```ini
# In /etc/yum.repos.d/rabbitmq-erlang.repo
[rabbitmq-erlang]
name=rabbitmq-erlang
baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/21/el/6
gpgcheck=1
gpgkey=https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc
repo_gpgcheck=0
enabled=1
```

#### Erlang 20.x

Note that [Erlang/OTP 20 is supported by RabbitMQ starting with version 3.6.11](https://groups.google.com/forum/#!msg/rabbitmq-users/_imbAavBYjY/S0LkV7b8CAAJ).

To use Erlang 20.x on CentOS 7:

```ini
# In /etc/yum.repos.d/rabbitmq-erlang.repo
[rabbitmq-erlang]
name=rabbitmq-erlang
baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/20/el/7
gpgcheck=1
gpgkey=https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc
repo_gpgcheck=0
enabled=1
```

To use Erlang 20.x on CentOS 6:

```ini
# In /etc/yum.repos.d/rabbitmq-erlang.repo
[rabbitmq-erlang]
name=rabbitmq-erlang
baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/20/el/6
gpgcheck=1
gpgkey=https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc
repo_gpgcheck=0
enabled=1
```

#### Erlang 19.x

To use Erlang 19.x on CentOS 7:

```ini
# In /etc/yum.repos.d/rabbitmq-erlang.repo
[rabbitmq-erlang]
name=rabbitmq-erlang
baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/19/el/7
gpgcheck=1
gpgkey=https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc
repo_gpgcheck=0
enabled=1
```

To use Erlang 19.x on CentOS 6:

```ini
# In /etc/yum.repos.d/rabbitmq-erlang.repo
[rabbitmq-erlang]
name=rabbitmq-erlang
baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/19/el/6
gpgcheck=1
gpgkey=https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc
repo_gpgcheck=0
enabled=1
```

### Package Cloud

Package Cloud supports a variety of options for RPM package installation: from Yum configuration to shell scripts
to Chef and Puppet.

See [Package Cloud repository installation](https://packagecloud.io/rabbitmq/erlang/install) page
for details.

To use the most recent version on CentOS 7:

``` ini
# In /etc/yum.repos.d/rabbitmq_erlang.repo
[rabbitmq_erlang]
name=rabbitmq_erlang
baseurl=https://packagecloud.io/rabbitmq/erlang/el/7/$basearch
repo_gpgcheck=1
gpgcheck=0
enabled=1
gpgkey=https://packagecloud.io/rabbitmq/erlang/gpgkey
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300

[rabbitmq_erlang-source]
name=rabbitmq_erlang-source
baseurl=https://packagecloud.io/rabbitmq/erlang/el/7/SRPMS
repo_gpgcheck=1
gpgcheck=0
enabled=1
gpgkey=https://packagecloud.io/rabbitmq/erlang/gpgkey
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
```

To use the most recent version on CentOS 6:

``` ini
# In /etc/yum.repos.d/rabbitmq_erlang.repo
[rabbitmq_erlang]
name=rabbitmq_erlang
baseurl=https://packagecloud.io/rabbitmq/erlang/el/6/$basearch
repo_gpgcheck=1
gpgcheck=0
enabled=1
gpgkey=https://packagecloud.io/rabbitmq/erlang/gpgkey
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300

[rabbitmq_erlang-source]
name=rabbitmq_erlang-source
baseurl=https://packagecloud.io/rabbitmq/erlang/el/6/SRPMS
repo_gpgcheck=1
gpgcheck=0
enabled=1
gpgkey=https://packagecloud.io/rabbitmq/erlang/gpgkey
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
metadata_expire=300
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
 * otp_mibs
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
# build a Centos 7 image and build the RPM using it
#
./build-image-and-rpm.sh 7 --no-cache

#
# To only build a CentOS 7 Docker image with necessary toolchain
#
 ./build-docker-image.sh 7 --no-cache
 
#
# To only build the RPM using an already built and available image
#
./build-rpm-in-docker 7
```

then find the result under `docker/build-dir-{CentOSVersion}/RPMS/x86_64/`,
e.g. `build-dir-7/RPMS/x86_64/`.

For CentOS 6, replace the `7` in the examples above with a `6`.


### Without Docker

You must be running an RPM-based distro (CentOS 7 or equivalent RHEL is highly recommended) for this to work.

    sudo make

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
 * [lib/otp_mibs/src/Makefile](https://github.com/erlang/otp/commits/maint/lib/otp_mibs/src/Makefile)
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


### Older Versions

The directory `versions` contains the patch files used for the older versions. Git repository
history can be useful as well.


## Copyright and License

(c) 2011-current Pivotal Software, Inc.

Released under the [Apache Software License 2.0](https://github.com/rabbitmq/erlang-rpm-packaging/blob/master/Erlang_ASL2_LICENSE.txt),
same as Erlang/OTP starting with 18.0.
