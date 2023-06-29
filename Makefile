# Copyright VMware, Inc. or its affiliantes, 2012-2022. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FINAL_OUTPUT_DIR=FINAL_RPMS

OTP_RELEASE=26.0.2

# Where official Erlang distribution files come from...
OTP_SRC_TGZ_FILE=OTP-$(OTP_RELEASE).tar.gz
ERLANG_DISTPOINT=https://github.com/erlang/otp/archive/OTP-$(OTP_RELEASE).tar.gz

# Where we will pull tarballs to
TARBALL_DIR=dist

TOP_DIR=$(shell pwd)
DEFINES=--define '_topdir $(TOP_DIR)' --define '_tmppath $(TOP_DIR)/tmp' --define '_sysconfdir /etc' --define '_localstatedir /var'

rpms:	clean erlang

build-deps:
	dnf update -y
	dnf install -y autoconf clang m4 openssl-devel ncurses-devel rpm-build rpmdevtools rpmlint tar wget zlib-devel systemd-devel make

prepare: build-deps
	mkdir -p BUILD SOURCES SPECS SRPMS RPMS tmp dist
ifneq ("$(wildcard /tmp/$(OTP_SRC_TGZ_FILE))","")
	# for faster turnaround time during development
	cp /tmp/$(OTP_SRC_TGZ_FILE) $(TARBALL_DIR)/$(OTP_SRC_TGZ_FILE)
else
	wget --no-clobber -O $(TARBALL_DIR)/$(OTP_SRC_TGZ_FILE) $(ERLANG_DISTPOINT)
endif
	tar -zxf $(TARBALL_DIR)/$(OTP_SRC_TGZ_FILE) -C dist
	cp $(TARBALL_DIR)/$(OTP_SRC_TGZ_FILE) SOURCES
	rm $(TARBALL_DIR)/$(OTP_SRC_TGZ_FILE)
	cp *.patch SOURCES
	cp erlang.spec SPECS
	cp Erlang_ASL2_LICENSE.txt SOURCES
	dnf update -y
	dnf install -y util-linux
	if test -f /etc/os-release; then \
		. /etc/os-release; \
		if test "$$ID" = 'centos' && test "$$VERSION_ID" -ge 7; then \
			dnf install -y rpm-sign; \
		fi; \
	fi

erlang: prepare
	mkdir -p $(FINAL_OUTPUT_DIR)
	rpmbuild -vv -bb --nodeps SPECS/erlang.spec $(DEFINES)
ifneq ($(SIGNING_KEY_ID),)
	setsid \
		rpm --addsign \
		--define '_signature gpg' \
		--define '_gpg_name $(SIGNING_KEY_ID)' \
		RPMS/*/*.rpm \
		< /dev/null
endif
	find RPMS -name "*.rpm" -exec sh -c 'mv {} `echo {} | sed 's#^RPMS\/noarch#$(FINAL_OUTPUT_DIR)#'`' ';'

clean:
	rm -rf BUILDROOT BUILD SOURCES SPECS SRPMS RPMS tmp $(FINAL_OUTPUT_DIR) dist
