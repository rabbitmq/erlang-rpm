FROM centos:{centosfrom}

RUN yum -y update && yum clean all

RUN yum install -y \
  autoconf \
  gcc \
  m4 \
  mercurial \
  openssl-devel \
  ncurses-devel \
  rpm-build \
  tar \
  wget \
  zlib-devel \
  make

RUN mkdir /build
CMD ["sh", "-c", "cd /build/build-dir-{centosfrom} && make"]
