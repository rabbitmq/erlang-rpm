# Zero-dependency Erlang RPM for RabbitMQ

This is a (virtually) zero dependency 64-bit Erlang RPM package that provides just enough to run RabbitMQ.
It may be easier to install than RPMs provided by Erlang Solutions in certain environments.
It may or may not be suitable for running other Erlang-based software or 3rd party RabbitMQ
plugins.

## Provided Erlang/OTP Versions

The package currently targets Erlang/OTP `19.0.x`,`19.1.x`,`19.2.x` and `19.3.x`. Only 64-bit packages are provided.

## Supported CentOS Versions

 * CentOS 7
 * CentOS 6

## Implicit OpenSSL/libcrypto Dependency

This package intentionally does not include OpenSSL/libcrypto. It must be provisioned separately.
Recent Erlang versions require a modern OpenSSL version, e.g. `1.0.1`.

## Release Artifacts

Binary packages can be obtained [from GitHub](https://github.com/rabbitmq/erlang-rpm/releases), [Package Cloud](https://packagecloud.io/rabbitmq/erlang), and [Bintray](https://bintray.com/rabbitmq/rpm/erlang).

To use the Bintray Yum repositories, here are the `.repo` configuration files:

* To use Erlang 18.x on CentOS 6:

    ```ini
    # In /etc/yum.repos.d/rabbitmq-erlang.repo
    [rabbitmq-erlang]
    name=rabbitmq-erlang
    baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/18/el/6
    gpgcheck=0
    repo_gpgcheck=0
    enabled=1
    ```

* To use Erlang 18.x on CentOS 7:

    ```ini
    # In /etc/yum.repos.d/rabbitmq-erlang.repo
    [rabbitmq-erlang]
    name=rabbitmq-erlang
    baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/18/el/7
    gpgcheck=0
    repo_gpgcheck=0
    enabled=1
    ```

* To use Erlang 19.x on CentOS 6:

    ```ini
    # In /etc/yum.repos.d/rabbitmq-erlang.repo
    [rabbitmq-erlang]
    name=rabbitmq-erlang
    baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/19/el/6
    gpgcheck=0
    repo_gpgcheck=0
    enabled=1
    ```

* To use Erlang 19.x on CentOS 7:

    ```ini
    # In /etc/yum.repos.d/rabbitmq-erlang.repo
    [rabbitmq-erlang]
    name=rabbitmq-erlang
    baseurl=https://dl.bintray.com/rabbitmq/rpm/erlang/19/el/7
    gpgcheck=0
    repo_gpgcheck=0
    enabled=1
    ```

## Building from Source

### With Docker
     	 
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
