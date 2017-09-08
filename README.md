# Zero-dependency Erlang RPM for RabbitMQ

This is a (virtually) zero dependency 64-bit Erlang RPM package that provides just enough to run RabbitMQ.
It may be easier to install than RPMs provided by Erlang Solutions in certain environments.
It may or may not be suitable for running other Erlang-based software or 3rd party RabbitMQ
plugins.

This package has an **implicit OpenSSL/libcrypto dependency** (see below).

## Provided Erlang/OTP Versions

The package currently targets Erlang/OTP `19.3.x` and `20.0.x`. Only 64-bit packages are provided.

`18.3.x`, `19.0.x`,`19.1.x`, and `19.2.x` are also available but get not updates unless
they address a critically important issue.

## Implicit OpenSSL/libcrypto Dependency

This package intentionally does not include OpenSSL/libcrypto. It must be provisioned separately.
Recent Erlang versions require a modern OpenSSL version, e.g. `1.0.1`.

## Supported CentOS Versions

Please note the **implicit OpenSSL/libcrypto dependency** section above.

 * CentOS 7
 * CentOS 6

## Release Artifacts

Binary packages can be obtained [from GitHub](https://github.com/rabbitmq/erlang-rpm/releases), [Package Cloud](https://packagecloud.io/rabbitmq/erlang), and [Bintray](https://bintray.com/rabbitmq/rpm/erlang).

Yum repositories are available from [Bintray](https://bintray.com/rabbitmq/rpm/erlang) and [Package Cloud](https://packagecloud.io/rabbitmq/erlang/).

### Bintray Yum Repositories

To use the Bintray Yum repositories, here are the `.repo` configuration files:

#### Erlang 20.x

To use Erlang 20.x on CentOS 6:

```ini
# In /etc/yum.repos.d/rabbitmq-erlang.repo
[rabbitmq-erlang]
name=rabbitmq-erlang
baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/20/el/6
gpgcheck=1
gpgkey=https://www.rabbitmq.com/rabbitmq-release-signing-key.asc
repo_gpgcheck=0
enabled=1
```

To use Erlang 20.x on CentOS 7:

```ini
# In /etc/yum.repos.d/rabbitmq-erlang.repo
[rabbitmq-erlang]
name=rabbitmq-erlang
baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/20/el/7
gpgcheck=1
gpgkey=https://www.rabbitmq.com/rabbitmq-release-signing-key.asc
repo_gpgcheck=0
enabled=1
```

#### Erlang 19.x

To use Erlang 19.x on CentOS 6:

```ini
# In /etc/yum.repos.d/rabbitmq-erlang.repo
[rabbitmq-erlang]
name=rabbitmq-erlang
baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/19/el/6
gpgcheck=1
gpgkey=https://www.rabbitmq.com/rabbitmq-release-signing-key.asc
repo_gpgcheck=0
enabled=1
```

To use Erlang 19.x on CentOS 7:

```ini
# In /etc/yum.repos.d/rabbitmq-erlang.repo
[rabbitmq-erlang]
name=rabbitmq-erlang
baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/19/el/7
gpgcheck=1
gpgkey=https://www.rabbitmq.com/rabbitmq-release-signing-key.asc
repo_gpgcheck=0
enabled=1
```

#### Erlang 18.x

To use Erlang 18.x on CentOS 6:

```ini
# In /etc/yum.repos.d/rabbitmq-erlang.repo
[rabbitmq-erlang]
name=rabbitmq-erlang
baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/18/el/6
gpgcheck=1
gpgkey=https://www.rabbitmq.com/rabbitmq-release-signing-key.asc
repo_gpgcheck=0
enabled=1
```

To use Erlang 18.x on CentOS 7:

```ini
# In /etc/yum.repos.d/rabbitmq-erlang.repo
[rabbitmq-erlang]
name=rabbitmq-erlang
baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/18/el/7
gpgcheck=1
gpgkey=https://www.rabbitmq.com/rabbitmq-release-signing-key.asc
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


## Building from Source

### With Docker

```sh
cd docker
#
# builds a CentOS 7 Docker image with necessary toolchain
#
 ./build-docker-image.sh 7 --no-cache
#
# builds the RPM in Docker
#
./build-rpm-in-docker 7
#
# Use build-image-and-rpm.sh to execute all scripts
# Ex: Centos 7 docker image and build RPM on the image:
#
./build-image-and-rpm.sh 7 --no-cache
#
# Ex: Centos 6 docker image and build RPM on the image:
#
./build-image-and-rpm.sh 6 --no-cache
#
#  --no-cache is optional. Use it to rebuild the docker image.
#
```

then find the result under `docker/build-dir-{centosversion}/RPMS/x86_64/`.
for example : `build-dir-7/RPMS/x86_64/`

### Without Docker

You must be running an RPMish distro for this to work.

    make

and see `RPMS/x86_64/`.

### Previous Versions

The directory `versions` contains the patch files used for the old versions.


## Copyright and License

(c) 2011-current Pivotal Software, Inc.

Released under the [Apache Software License 2.0](https://github.com/rabbitmq/erlang-rpm-packaging/blob/master/Erlang_ASL2_LICENSE.txt),
same as Erlang/OTP starting with 18.0.
