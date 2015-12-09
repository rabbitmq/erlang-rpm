# Zero-dependency Erlang RPM for RabbitMQ

This is a zero dependency 64-bit Erlang RPM package that provides just enough to run RabbitMQ.
It may be easier to install than RPMs provided by Erlang Solutions in certain environments.

## Provided Erlang/OTP Versions

The package currently targets Erlang/OTP 18.1 (64-bit only).

## Supported CentOS Versions

 * CentOS 6
 * CentOS 7

## Release Artifacts

Package builds are [available from rabbitmq.com](http://www.rabbitmq.com/releases/erlang/)
and [from GitHub](https://github.com/rabbitmq/erlang-rpm/releases).

## Building

### With Docker
     	 
     cd docker
     # builds a CentOS 7.1.1503 Docker image with necessary toolchain
      ./build-docker-image.sh 7.1.1503 --no-cache
     # builds the RPM in Docker
     ./build-rpm-in-docker.sh 7.1.1503
    
     # Use build-image-and-rpm.sh to execute all scripts 
     # Ex: Centos 7.1.1503 docker image and build RPM on the image:	
     ./build-image-and-rpm.sh 7.1.1503 --no-cache
     
     # Ex: Centos 6 docker image and build RPM on the image::	
     ./build-image-and-rpm.sh 6 --no-cache
      
       --no-cache is optional. Use it to rebuild the docker image.

then find the result under `docker/build-dir-{centosversion}/RPMS/x86_64/`. 
for example : `build-dir-7.1.1503/RPMS/x86_64/`

### Without Docker

You must be running an RPMish distro for this to work.

    make

and see `RPMS/x86_64/`.

## Copyright and License

(c) 2011-2015 Pivotal Software, Inc.

Released under the [Apache Software License 2.0](https://github.com/rabbitmq/erlang-rpm-packaging/blob/master/Erlang_ASL2_LICENSE.txt),
same as Erlang/OTP starting with 18.0.
