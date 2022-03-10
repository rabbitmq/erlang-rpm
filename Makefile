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

OTP_RELEASE=24.2.2

# Where official Erlang distribution files come from...
OTP_SRC_TGZ_FILE=OTP-$(OTP_RELEASE).tar.gz
ERLANG_DISTPOINT=https://github.com/erlang/otp/archive/OTP-$(OTP_RELEASE).tar.gz

# Where we will pull tarballs to
TARBALL_DIR=dist

TOP_DIR=$(shell pwd)
DEFINES=--define '_topdir $(TOP_DIR)' --define '_tmppath $(TOP_DIR)/tmp' --define '_sysconfdir /etc' --define '_localstatedir /var'

rpms:	clean erlang

prepare:
	mkdir -p BUILD SOURCES SPECS SRPMS RPMS tmp dist
	wget -O $(TARBALL_DIR)/$(OTP_SRC_TGZ_FILE) $(ERLANG_DISTPOINT)#
	tar -zxf $(TARBALL_DIR)/$(OTP_SRC_TGZ_FILE) -C dist
	cp $(TARBALL_DIR)/$(OTP_SRC_TGZ_FILE) SOURCES
	rm $(TARBALL_DIR)/$(OTP_SRC_TGZ_FILE)
	cp *.patch SOURCES
	cp erlang.spec SPECS
	cp Erlang_ASL2_LICENSE.txt SOURCES
	yum update -y
	yum install -y util-linux
	if test -f /etc/os-release; then \
		. /etc/os-release; \
		if test "$$ID" = 'centos' && test "$$VERSION_ID" -ge 7; then \
			yum install -y rpm-sign; \
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
