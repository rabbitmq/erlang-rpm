#!/usr/bin/env sh

all_rpms_dir="all_rpms"

mkdir -p "$all_rpms_dir"

build_and_fetch_rpm_for() {
  distribution=$1
  ./build-image-and-rpm.sh "$distribution"
  cp pkg-build-dir/RPMS/*/erlang-* "$all_rpms_dir"
}

# These cover CentOS Stream, Rocky Linux, Alma Linux, Oracle Linux
# of the same respective version
build_and_fetch_rpm_for "stream9"
build_and_fetch_rpm_for "stream8"
# These distributions cannot use CentOS Stream packages
build_and_fetch_rpm_for "al2023"
build_and_fetch_rpm_for "fc38"

