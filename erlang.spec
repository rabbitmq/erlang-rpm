# Copyright VMware, Inc. or its affiliantes, 2012-2020. All Rights Reserved.
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

%global upstream_ver 24.0.5
%global package_ver  24.0.5
%global package_ver_release 1

%define OSL_File_Name                   Erlang_ASL2_LICENSE.txt

Name:		erlang
Version:	%{package_ver}
Release:	%{package_ver_release}%{?dist}
Summary:	Minimalistic Erlang/OTP distribution that provides just enough for running RabbitMQ

Group:		Development/Languages
License:	ASL 2.0
URL:		https://www.erlang.org
Source0:	https://github.com/erlang/otp/archive/OTP-%{upstream_ver}.tar.gz
Source2:        %{OSL_File_Name}
Vendor:		VMware, Inc.


#   Do not format man-pages and do not install miscellaneous
Patch1: otp-0001-Do-not-format-man-pages-and-do-not-install-miscellan.patch
#   Do not install C sources
Patch2: otp-0002-Do-not-install-C-sources.patch
#   Do not install erlang sources
Patch3: otp-0003-Do-not-install-erlang-sources.patch

# BuildRoot not strictly needed since F10, but keep it for spec file robustness
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	m4
BuildRequires:	autoconf
# will install gcc and gcc-c++ as dependencies
BuildRequires:  clang

Obsoletes: erlang-docbuilder

%description
This is a minimal packaging of Erlang produced by VMware, Inc. to support
running RabbitMQ. Compared to the community Erlang packaging it is
monolithic, has fewer dependencies, and has lower disk and memory
overhead. Many applications from Erlang Open Telecom Platform (OTP)
have been removed. The following applications remain: asn1, compiler,
crypto, erl_interface, erts, inets, kernel, mnesia, os_mon,
public_key, reltool, runtime_tools, sasl, snmp, ssl, stdlib,
syntax_tools and xmerl.

%define _license_file %{_builddir}/otp-OTP-%{upstream_ver}/`basename %{S:2}`


%prep
%setup -q -n otp-OTP-%{upstream_ver}

%patch1 -p1 -b .Do_not_format_man_pages_and_do_not_install_miscellan
%patch2 -p1 -b .Do_not_install_C_sources
%patch3 -p1 -F2 -b .Do_not_install_erlang_sources

# Fix 664 file mode
chmod 644 lib/kernel/examples/uds_dist/c_src/Makefile
chmod 644 lib/kernel/examples/uds_dist/src/Makefile
chmod 644 lib/ssl/examples/certs/Makefile
chmod 644 lib/ssl/examples/src/Makefile


%build
%if ! (0%{?rhel} && 0%{?rhel} <= 6)
%global conf_flags --enable-shared-zlib --enable-systemd --without-javac --without-odbc
%else
%global conf_flags --enable-shared-zlib --without-javac --without-odbc
%endif

# autoconf
./otp_build autoconf

%ifarch sparcv9 sparc64
CFLAGS="$RPM_OPT_FLAGS -mcpu=ultrasparc -fno-strict-aliasing" %configure %{conf_flags}
%else
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" %configure %{conf_flags}
%endif


# remove pre-built stuff
make clean

cp %{S:2} %{_license_file}

touch lib/common_test/SKIP
touch lib/debugger/SKIP
touch lib/dialyzer/SKIP
touch lib/diameter/SKIP
touch lib/edoc/SKIP
touch lib/et/SKIP
touch lib/erl_docgen/SKIP
touch lib/ftp/SKIP
touch lib/jinterface/SKIP
touch lib/megaco/SKIP
touch lib/observer/SKIP
touch lib/odbc/SKIP
touch lib/ssh/SKIP
touch lib/tftp/SKIP
touch lib/wx/SKIP

make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

# Do not install info files - they are almost empty and useless
find $RPM_BUILD_ROOT%{_libdir}/erlang -type f -name info -exec rm -f {} \;

# fix 0775 permission on some directories
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/erlang/bin

# Win32-specific man-pages
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/man/man1/erlsrv.*
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/man/man1/werl.*
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/man/man3/win32reg.*

# remove empty directory
rm -r $RPM_BUILD_ROOT%{_libdir}/erlang/erts-*/man

# remove outdated script
rm -f $RPM_BUILD_ROOT%{_libdir}/erlang/Install

# Replace identical executables with symlinks
for exe in $RPM_BUILD_ROOT%{_libdir}/erlang/erts-*/bin/*
do
	base="$(basename "$exe")"
	next="$RPM_BUILD_ROOT%{_libdir}/erlang/bin/${base}"
	rel="$(echo "$exe" | sed "s,^$RPM_BUILD_ROOT%{_libdir}/erlang/,../,")"
	if cmp "$exe" "$next"; then
		ln -sf "$rel" "$next"
	fi
done
for exe in $RPM_BUILD_ROOT%{_libdir}/erlang/bin/*
do
	base="$(basename "$exe")"
	next="$RPM_BUILD_ROOT%{_bindir}/${base}"
	rel="$(echo "$exe" | sed "s,^$RPM_BUILD_ROOT,,")"
	if cmp "$exe" "$next"; then
		ln -sf "$rel" "$next"
	fi
done

rm -rf $RPM_BUILD_ROOT%{_bindir}/ct_run
rm -rf $RPM_BUILD_ROOT%{_bindir}/dialyzer
rm -rf $RPM_BUILD_ROOT%{_bindir}/run_test
rm -rf $RPM_BUILD_ROOT%{_bindir}/typer
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/bin/ct_run
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/bin/erl_call
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/bin/dialyzer
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/bin/run_test
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/bin/typer
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/erts-*/bin/ct_run
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/erts-*/bin/erl_call
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/erts-*/bin/dialyzer
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/erts-*/bin/typer
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/erts-*/bin/yielding_c_fun
rm -rf $RPM_BUILD_ROOT%{_libdir}/erlang/lib/*/examples

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)

%doc %{OSL_File_Name}

%dir %{_libdir}/erlang/lib/asn1-*/
%{_libdir}/erlang/lib/asn1-*/ebin
%{_libdir}/erlang/lib/asn1-*/priv
%{_libdir}/erlang/lib/asn1-*/src


%{_libdir}/erlang/lib/compiler-*/


%{_libdir}/erlang/lib/crypto-*/

%dir %{_libdir}/erlang/lib/eldap-*/
%{_libdir}/erlang/lib/eldap-*/asn1
%{_libdir}/erlang/lib/eldap-*/ebin
%{_libdir}/erlang/lib/eldap-*/include
%{_libdir}/erlang/lib/eldap-*/src

%{_libdir}/erlang/lib/eunit-*/

%{_libdir}/erlang/lib/erl_interface-*/


%dir %{_libdir}/erlang/
%dir %{_libdir}/erlang/bin/
%dir %{_libdir}/erlang/lib/
%dir %{_libdir}/erlang/releases/
%{_bindir}/epmd
%{_bindir}/erl
%{_bindir}/erlc
%{_bindir}/escript
%{_bindir}/run_erl
%{_bindir}/to_erl
%{_libdir}/erlang/bin/epmd
%{_libdir}/erlang/bin/erl
%{_libdir}/erlang/bin/erlc
%{_libdir}/erlang/bin/escript
%{_libdir}/erlang/bin/no_dot_erlang.boot
%{_libdir}/erlang/bin/run_erl
%{_libdir}/erlang/bin/start
%{_libdir}/erlang/bin/start.boot
%{_libdir}/erlang/bin/start.script
%{_libdir}/erlang/bin/start_clean.boot
%{_libdir}/erlang/bin/start_erl
%{_libdir}/erlang/bin/start_sasl.boot
%{_libdir}/erlang/bin/to_erl
%dir %{_libdir}/erlang/erts-*/bin
%{_libdir}/erlang/erts-*/bin/beam.smp
%{_libdir}/erlang/erts-*/bin/erl_child_setup
%{_libdir}/erlang/erts-*/bin/dyn_erl
%{_libdir}/erlang/erts-*/bin/epmd
%{_libdir}/erlang/erts-*/bin/erl
%{_libdir}/erlang/erts-*/bin/erl.src
%{_libdir}/erlang/erts-*/bin/erlc
%{_libdir}/erlang/erts-*/bin/erlexec
%{_libdir}/erlang/erts-*/bin/escript
%{_libdir}/erlang/erts-*/bin/heart
%{_libdir}/erlang/erts-*/bin/inet_gethost
%{_libdir}/erlang/erts-*/bin/run_erl
%{_libdir}/erlang/erts-*/bin/start
%{_libdir}/erlang/erts-*/bin/start.src
%{_libdir}/erlang/erts-*/bin/start_erl.src
%{_libdir}/erlang/erts-*/bin/to_erl
%{_libdir}/erlang/erts-*/include
%{_libdir}/erlang/erts-*/lib
%{_libdir}/erlang/erts-*/src
%{_libdir}/erlang/lib/erts-*/
%{_libdir}/erlang/releases/*
%{_libdir}/erlang/usr/


%dir %{_libdir}/erlang/lib/inets-*/
%{_libdir}/erlang/lib/inets-*/ebin
%{_libdir}/erlang/lib/inets-*/include
%{_libdir}/erlang/lib/inets-*/priv
%{_libdir}/erlang/lib/inets-*/src


%dir %{_libdir}/erlang/lib/kernel-*/
%{_libdir}/erlang/lib/kernel-*/ebin
%{_libdir}/erlang/lib/kernel-*/include
%{_libdir}/erlang/lib/kernel-*/src


%dir %{_libdir}/erlang/lib/mnesia-*/
%{_libdir}/erlang/lib/mnesia-*/ebin
%{_libdir}/erlang/lib/mnesia-*/include
%{_libdir}/erlang/lib/mnesia-*/src


%{_libdir}/erlang/lib/os_mon-*/

%{_libdir}/erlang/lib/parsetools-*/

%{_libdir}/erlang/lib/public_key-*/


%dir %{_libdir}/erlang/lib/reltool-*/
%{_libdir}/erlang/lib/reltool-*/ebin
%{_libdir}/erlang/lib/reltool-*/src

%dir %{_libdir}/erlang/lib/syntax_tools-*/
%{_libdir}/erlang/lib/syntax_tools-*/ebin
%{_libdir}/erlang/lib/syntax_tools-*/include

%{_libdir}/erlang/lib/runtime_tools-*/


%dir %{_libdir}/erlang/lib/sasl-*/
%{_libdir}/erlang/lib/sasl-*/ebin
%{_libdir}/erlang/lib/sasl-*/src


%dir %{_libdir}/erlang/lib/snmp-*/
%{_libdir}/erlang/lib/snmp-*/bin
%{_libdir}/erlang/lib/snmp-*/ebin
%{_libdir}/erlang/lib/snmp-*/include
%{_libdir}/erlang/lib/snmp-*/mibs
%{_libdir}/erlang/lib/snmp-*/priv
%{_libdir}/erlang/lib/snmp-*/src


%dir %{_libdir}/erlang/lib/ssl-*/
%{_libdir}/erlang/lib/ssl-*/ebin
%{_libdir}/erlang/lib/ssl-*/src


%dir %{_libdir}/erlang/lib/stdlib-*/
%{_libdir}/erlang/lib/stdlib-*/ebin
%{_libdir}/erlang/lib/stdlib-*/include
%{_libdir}/erlang/lib/stdlib-*/src

%{_libdir}/erlang/lib/tools-*/

%{_libdir}/erlang/lib/xmerl-*/


%changelog
* Fri Jul 30 2021 Michael Klishin <klishinm@vmware.com> - 24.0.5
- Update to Erlang/OTP 24.0.5.

* Thu Jul 22 2021 Michael Klishin <klishinm@vmware.com> - 24.0.4
- Update to Erlang/OTP 24.0.4.

* Mon Jun 28 2021 Michael Klishin <klishinm@vmware.com> - 24.0.3
- Update to Erlang/OTP 24.0.3.

* Tue Jun 01 2021 Michael Klishin <klishinm@vmware.com> - 24.0.2
- Update to Erlang/OTP 24.0.2.

* Fri May 21 2021 Michael Klishin <klishinm@vmware.com> - 24.0.1
- Update to Erlang/OTP 24.0.1.

* Wed May 12 2021 Michael Klishin <klishinm@vmware.com> - 24.0
- Update to Erlang/OTP 24.0.

* Thu May 6 2021 Michael Klishin <klishinm@vmware.com> - 23.3.3
- Update to Erlang/OTP 23.3.3.

* Wed Apr 28 2021 Michael Klishin <klishinm@vmware.com> - 23.3.2
- Update to Erlang/OTP 23.3.2.

* Wed Mar 31 2021 Michael Klishin <klishinm@vmware.com> - 23.3.1
- Update to Erlang/OTP 23.3.1.

* Wed Mar 24 2021 Michael Klishin <klishinm@vmware.com> - 23.3
- Update to Erlang/OTP 23.3.

* Thu Mar 4 2021 Jean-Sébastien Pédron <jean-sebastien@rabbitmq.com> - 23.2.7-2
- Restore the creation of the -debuginfo package.

* Wed Mar 3 2021 Michael Klishin <klishinm@vmware.com> - 23.2.7-1
- Update to Erlang/OTP 23.2.7.

* Mon Mar 1 2021 Michael Klishin <klishinm@vmware.com> - 23.2.6
- Update to Erlang/OTP 23.2.6.

* Sat Feb 20 2021 Michael Klishin <klishinm@vmware.com> - 23.2.5
- Update to Erlang/OTP 23.2.5.

* Wed Feb 10 2021 Michael Klishin <klishinm@vmware.com> - 23.2.4
- Update to Erlang/OTP 23.2.4.

* Mon Feb 1 2021 Michael Klishin <klishinm@vmware.com> - 23.2.3
- Update to Erlang/OTP 23.2.3.

* Fri Dec 25 2020 Michael Klishin <klishinm@vmware.com> - 23.2.1
- Update to Erlang/OTP 23.2.1.

* Mon Dec 7 2020 Michael Klishin <klishinm@vmware.com> - 23.1.5
- Update to Erlang/OTP 23.1.5.

* Mon Nov 23 2020 Michael Klishin <klishinm@vmware.com> - 23.1.4
- Update to Erlang/OTP 23.1.4.

* Tue Nov 17 2020 Michael Klishin <klishinm@vmware.com> - 23.1.3
- Update to Erlang/OTP 23.1.3.

* Thu Nov 5 2020 Michael Klishin <klishinm@vmware.com> - 23.1.2
- Update to Erlang/OTP 23.1.2.

* Sat Oct 3 2020 Michael Klishin <klishinm@vmware.com> - 23.1.1
- Update to Erlang/OTP 23.1.1.

* Wed Sep 23 2020 Michael Klishin <klishinm@vmware.com> - 23.1
- Update to Erlang/OTP 23.1.

* Mon Sep 14 2020 Michael Klishin <klishinm@vmware.com> - 23.0.4
- Update to Erlang/OTP 23.0.4.

* Tue Jul 21 2020 Michael Klishin <mklishin@pivotal.io> - 23.0.3
- Update to Erlang/OTP 23.0.3.

* Tue Jun 2 2020 Michael Klishin <mklishin@pivotal.io> - 23.0.2
- Update to Erlang/OTP 23.0.2.

* Thu May 21 2020 Michael Klishin <mklishin@pivotal.io> - 23.0.1
- Update to Erlang/OTP 23.0.1.

* Wed May 13 2020 Michael Klishin <mklishin@pivotal.io> - 23.0
- Update to Erlang/OTP 23.0.

* Tue Apr 28 2020 Michael Klishin <mklishin@pivotal.io> - 22.3.3
- Update to Erlang/OTP 22.3.3.

* Sat Apr 11 2020 Michael Klishin <mklishin@pivotal.io> - 22.3.2
- Update to Erlang/OTP 22.3.2.

* Tue Apr 7 2020 Michael Klishin <mklishin@pivotal.io> - 22.3.1
- Update to Erlang/OTP 22.3.1.

* Wed Mar 18 2020 Michael Klishin <mklishin@pivotal.io> - 22.3
- Update to Erlang/OTP 22.3.

* Wed Mar 4 2020 Michael Klishin <mklishin@pivotal.io> - 22.2.8
- Update to Erlang/OTP 22.2.8.

* Wed Feb 19 2020 Michael Klishin <mklishin@pivotal.io> - 22.2.7
- Update to Erlang/OTP 22.2.7.

* Wed Feb 5 2020 Michael Klishin <mklishin@pivotal.io> - 22.2.6
- Update to Erlang/OTP 22.2.6.

* Tue Feb 4 2020 Michael Klishin <mklishin@pivotal.io> - 22.2.5
- Update to Erlang/OTP 22.2.5.

* Tue Jan 28 2020 Michael Klishin <mklishin@pivotal.io> - 22.2.4
- Update to Erlang/OTP 22.2.4.

* Fri Jan 24 2020 Michael Klishin <mklishin@pivotal.io> - 22.2.3
- Update to Erlang/OTP 22.2.3.

* Wed Jan 15 2020 Michael Klishin <mklishin@pivotal.io> - 22.2.2
- Update to Erlang/OTP 22.2.2.

* Thu Dec 19 2019 Michael Klishin <mklishin@pivotal.io> - 22.2.1
- Update to Erlang/OTP 22.2.1.

* Tue Dec 10 2019 Michael Klishin <mklishin@pivotal.io> - 22.2
- Update to Erlang/OTP 22.2.

* Mon Nov 25 2019 Michael Klishin <mklishin@pivotal.io> - 22.1.8
- Update to Erlang/OTP 22.1.8.

* Mon Nov 11 2019 Michael Klishin <mklishin@pivotal.io> - 22.1.7
- Update to Erlang/OTP 22.1.7.

* Thu Nov 7 2019 Michael Klishin <mklishin@pivotal.io> - 22.1.6
- Update to Erlang/OTP 22.1.6.

* Mon Oct 28 2019 Michael Klishin <mklishin@pivotal.io> - 22.1.5
- Update to Erlang/OTP 22.1.5.

* Wed Oct 23 2019 Michael Klishin <mklishin@pivotal.io> - 22.1.4
- Update to Erlang/OTP 22.1.4.

* Sat Oct 12 2019 Michael Klishin <mklishin@pivotal.io> - 22.1.3
- Update to Erlang/OTP 22.1.3.

* Wed Oct 9 2019 Michael Klishin <mklishin@pivotal.io> - 22.1.2
- Update to Erlang/OTP 22.1.2.

* Fri Sep 27 2019 Michael Klishin <mklishin@pivotal.io> - 22.1.1
- Update to Erlang/OTP 22.1.1.

* Tue Sep 17 2019 Michael Klishin <mklishin@pivotal.io> - 22.1
- Update to Erlang/OTP 22.1.

* Thu Jul 11 2019 Michael Klishin <mklishin@pivotal.io> - 22.0.7
- Update to Erlang/OTP 22.0.7.

* Wed Jul 10 2019 Michael Klishin <mklishin@pivotal.io> - 22.0.6
- Update to Erlang/OTP 22.0.6.

* Thu Jul 4 2019 Michael Klishin <mklishin@pivotal.io> - 22.0.5
- Update to Erlang/OTP 22.0.5.

* Tue Jun 18 2019 Michael Klishin <mklishin@pivotal.io> - 22.0.4
- Update to Erlang/OTP 22.0.4

* Thu Jun 13 2019 Michael Klishin <mklishin@pivotal.io> - 22.0.3
- Update to Erlang/OTP 22.0.3.

* Mon Jun 03 2019 Michael Klishin <mklishin@pivotal.io> - 22.0.2
- Update to Erlang/OTP 22.0.2.

* Tue May 21 2019 Michael Klishin <mklishin@pivotal.io> - 22.0.1
- Update to Erlang/OTP 22.0.1.

* Tue May 14 2019 Michael Klishin <mklishin@pivotal.io> - 22.0
- Update to Erlang/OTP 22.0.

* Fri May 10 2019 Michael Klishin <mklishin@pivotal.io> - 21.3.7.1
- Update to Erlang/OTP 21.3.7.1.

* Sun Apr 28 2019 Michael Klishin <mklishin@pivotal.io> - 21.3.7
- Update to Erlang/OTP 21.3.7.

* Thu Apr 18 2019 Michael Klishin <mklishin@pivotal.io> - 21.3.6
- Update to Erlang/OTP 21.3.6.

* Tue Apr 16 2019 Michael Klishin <mklishin@pivotal.io> - 21.3.5
- Update to Erlang/OTP 21.3.5.

* Sat Apr 13 2019 Michael Klishin <mklishin@pivotal.io> - 21.3.4
- Update to Erlang/OTP 21.3.4.

* Mon Apr 1 2019 Michael Klishin <mklishin@pivotal.io> - 21.3.3
- Update to Erlang/OTP 21.3.3.

* Fri Mar 22 2019 Michael Klishin <mklishin@pivotal.io> - 21.3.2
- Update to Erlang/OTP 21.3.2.

* Tue Mar 19 2019 Michael Klishin <mklishin@pivotal.io> - 21.3.1
- Update to Erlang/OTP 21.3.1.

* Thu Mar 14 2019 Michael Klishin <mklishin@pivotal.io> - 21.3
- Update to Erlang/OTP 21.3.

* Fri Mar 8 2019 Michael Klishin <mklishin@pivotal.io> - 21.2.7
- Update to Erlang/OTP 21.2.7.

* Mon Feb 18 2019 Michael Klishin <mklishin@pivotal.io> - 21.2.6
- Update to Erlang/OTP 21.2.6.

* Tue Feb 5 2019 Michael Klishin <mklishin@pivotal.io> - 21.2.5
- Update to Erlang/OTP 21.2.5.

* Fri Jan 25 2019 Michael Klishin <mklishin@pivotal.io> - 21.2.4
- Update to Erlang/OTP 21.2.4.

* Wed Jan 16 2019 Michael Klishin <mklishin@pivotal.io> - 21.2.3
- Update to Erlang/OTP 21.2.3.

* Sat Dec 29 2018 Michael Klishin <mklishin@pivotal.io> - 21.2.2
- Update to Erlang/OTP 21.2.2.

* Fri Dec 28 2018 Michael Klishin <mklishin@pivotal.io> - 21.2.1
- Update to Erlang/OTP 21.2.1.

* Wed Dec 12 2018 Michael Klishin <mklishin@pivotal.io> - 21.2
- Update to Erlang/OTP 21.2.

* Fri Nov 30 2018 Michael Klishin <mklishin@pivotal.io> - 21.1.4
- Update to Erlang/OTP 21.1.4.

* Sat Nov 24 2018 Michael Klishin <mklishin@pivotal.io> - 21.1.3
- Update to Erlang/OTP 21.1.3.

* Thu Nov 22 2018 Michael Klishin <mklishin@pivotal.io> - 21.1.2
- Update to Erlang/OTP 21.1.2.

* Tue Nov 6 2018 Gabriele Santomaggio <g.santomaggio@gmil.com>
- Add patch file for crypo.c

* Wed Oct 24 2018 Michael Klishin <mklishin@pivotal.io> - 21.1.1
- Update to Erlang/OTP 21.1.1.

* Tue Oct 9 2018 Jean-Sébastien Pédron <jean-sebastien@rabbitmq.com> - 21.1-2
- Remove the too generic `Provides: erlang` line which prevented version requirement in packages depending on Erlang from working.

* Tue Sep 25 2018 Michael Klishin <mklishin@pivotal.io> - 21.1
- Update to Erlang/OTP 21.1.

* Wed Sep 12 2018 Michael Klishin <mklishin@pivotal.io> - 21.0.9
- Update to Erlang/OTP 21.0.9.

* Thu Sep 6 2018 Michael Klishin <mklishin@pivotal.io> - 21.0.8
- Update to Erlang/OTP 21.0.8.

* Mon Sep 3 2018 Michael Klishin <mklishin@pivotal.io> - 21.0.7
- Update to Erlang/OTP 21.0.7.

* Wed Aug 29 2018 Michael Klishin <mklishin@pivotal.io> - 21.0.6
- Update to Erlang/OTP 21.0.6.

* Sun Aug 12 2018 Michael Klishin <mklishin@pivotal.io> - 21.0.5
- Update to Erlang/OTP 21.0.5.

* Thu Jul 26 2018 Michael Klishin <mklishin@pivotal.io> - 21.0.4
- Update to Erlang/OTP 21.0.4.

* Fri Jul 13 2018 Michael Klishin <mklishin@pivotal.io> - 21.0.3
- Update to Erlang/OTP 21.0.3.

* Fri Jul 6 2018 Michael Klishin <mklishin@pivotal.io> - 21.0.2
- Update to Erlang/OTP 21.0.2.

* Wed Jun 20 2018 Michael Klishin <mklishin@pivotal.io> - 21.0
- Update to Erlang/OTP 21.0.

* Wed Jun 20 2018 Michael Klishin <mklishin@pivotal.io> - 20.3.8
- Update to Erlang/OTP 20.3.8.

* Fri Jun 8 2018 Michael Klishin <mklishin@pivotal.io> - 20.3.7
- Update to Erlang/OTP 20.3.7.

* Fri May 18 2018 Michael Klishin <mklishin@pivotal.io> - 20.3.6
- Update to Erlang/OTP 20.3.6.

* Fri Apr 20 2018 Michael Klishin <mklishin@pivotal.io> - 20.3.4
- Update to Erlang/OTP 20.3.4.

* Wed Mar 14 2018 Michael Klishin <mklishin@pivotal.io> - 20.3
- Update to Erlang/OTP 20.3.

* Tue Feb 13 2018 Michael Klishin <mklishin@pivotal.io> - 20.2.3
- Update to Erlang/OTP 20.2.3.

* Sun Jan 14 2018 Michael Klishin <mklishin@pivotal.io> - 20.2.2
- Update to Erlang/OTP 20.2.2.

* Wed Dec 13 2017 Michael Klishin <mklishin@pivotal.io> - 20.1.7.1
- Update to Erlang/OTP 20.1.7.

* Wed Nov 29 2017 Michael Klishin <mklishin@pivotal.io> - 20.1.7
- Update to Erlang/OTP 20.1.7.

* Fri Nov 10 2017 Michael Klishin <mklishin@pivotal.io> - 20.1.5
- Update to Erlang/OTP 20.1.5.

* Thu Nov 2 2017 Michael Klishin <mklishin@pivotal.io> - 20.1.4
- Update to Erlang/OTP 20.1.4.

* Wed Oct 11 2017 Michael Klishin <mklishin@pivotal.io> - 20.1.2
- Update to Erlang/OTP 20.1.2.

* Fri Oct 6 2017 Michael Klishin <mklishin@pivotal.io> - 20.1.1
- Update to Erlang/OTP 20.1.1.

* Tue Sep 26 2017 Michael Klishin <mklishin@pivotal.io> - 20.1.0
- Update to Erlang/OTP 20.1.

* Thu Sep 14 2017 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 20.0.5
- Update to Erlang/OTP 20.0.5.

* Fri Aug 25 2017 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 20.0.4
- Update to Erlang/OTP 20.0.4.

* Thu Aug 24 2017 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 20.0.3
- Update to Erlang/OTP 20.0.3.

* Thu Jul 27 2017 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 20.0.2
- Update to Erlang/OTP 20.0.2.

* Thu Jul 6 2017 Jean-Sébastien Pédron <jean-sebastien@rabbitmq.com> - 20.0.1-1
- Update to Erlang/OTP 20.0.1.

* Mon Jul 3 2017 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.3.6.1
- update for 19.3.6.1

* Thu Jun 8 2017 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.3.6
- update for 19.3.6

* Mon Jun 5 2017 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.3.5
- update for 19.3.5

* Fri May 12 2017 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.3.4
- update for 19.3.4

* Tue May 2 2017 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.3.3
- update for 19.3.3

* Mon Apr 24 2017 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.3.2
- update for 19.3.2

* Tue Apr 4 2017 Michael Klishin <mklishin@pivotal.io> - 19.3.1
- update for 19.3.1

* Tue Mar 14 2017 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.3
- update for 19.3

* Wed Feb 8 2017 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.2.3
- update for 19.2.3

* Thu Feb 2 2017 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.2.2
- update for 19.2.2

* Fri Jan 20 2017 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.2.1
- update for 19.2.1

* Wed Dec 14 2016 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.2
- update for 19.2

* Mon Nov 14 2016 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.1.6
- update for 19.1.6

* Mon Oct 24 2016 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.1.5
- update for 19.1.5

* Thu Oct 13 2016 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.1.3
- update for 19.1.3

* Mon Oct 3 2016 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.1.1
- update for 19.1.1

* Thu Sep 22 2016 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.1
- update for 19.1

* Wed Sep 14 2016 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.0.7
- update for 19.0.7

* Wed Sep 14 2016 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.0.6
- update for 19.0.6

* Sun Aug 14 2016 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.0.4
- update for 19.0.4

* Sun Jul 17 2016 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 19.0
- update for 19.0

* Tue Jul 05 2016 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 18.3.4
- update for 18.3.4

* Mon Mar 21 2016 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 18.3
- update for 18.3

* Mon Dec 21 2015 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 18.2.1
- update for 18.2.1

* Fri Oct 23 2015 Gabriele Santomaggio <gabriele.santomaggio@erlang-solutions.com> - 18.1
- Fixed build for 18.1

* Tue Oct 13 2015 Michael Klishin <michael@rabbitmq.com> - 18.1
- Updates for 18.1

* Thu Sep 06 2012 Emile Joubert <emile@rabbitmq.com> - R15B-02.1
- Updates for R15B02
- Minimised build requirements
- Removed docs

* Wed Apr 25 2012 Stuart Williams <swilliams@vmware.com> - erlang-for-rabbitmq
- Minimised & removed dependencies not required for RabbitMQ and restored single package build.

* Tue Feb 07 2012 Peter Lemenkov <lemenkov@gmail.com> - R15B-00.1
- Ver. R15B

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - R14B-04.1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Aug 07 2011 Peter Lemenkov <lemenkov@gmail.com> - R14B-04.1
- Ver. R14B04

* Sun Aug 07 2011 Peter Lemenkov <lemenkov@gmail.com> - R14B-03.3
- Use prebuilt docs on EL-[56] also

* Thu Jul 21 2011 Peter Lemenkov <lemenkov@gmail.com> - R14B-03.2
- Fixed building on F-15

* Wed Jul 20 2011 Peter Lemenkov <lemenkov@gmail.com> - R14B-03.1
- Ver. R14B03
- New module - diameter
- Several new examples directories

* Fri Apr  1 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - R14B-02.2
- Work around fop-1.0-14.fc16 bug (#689930) by using prebuilt docs for f16/rawhide

* Mon Mar 21 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - R14B-02.1
- snmp-4.19 (R14B02) ships lib/snmp/bin/snmpc
- inets-5.5.2 puts *.hrl in include/
- install/symlink *.jar into %%{_javadir} (#679031)
- Update to upstream maintenance release R14B02

* Sat Feb 12 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - R14B-01.5
- erlang-doc does not really require erlang base package (#629723)
- Add %%{?_isa} for all explicit "Requires:"

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - R14B-01.4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - R14B-01.4
- Adapt %%files: Add wxSystemSettings.3 man page
- Adapt %%files for change from run_test to ct_run
- Remove rpaths from lib/ssl-*/bin/esock_ssl
- Update erlang.spec and otp-00*.patch without numbers
- otp-get-patches.sh: Remove patch numbering

* Sun Jan 30 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - R14B-01.3
- Add "buffer overflow during build" fix (#663260)

* Wed Dec 15 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - R14B-01.2
- Update to rebased patches

* Mon Dec 13 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - R14B-01.1
- Update to upstream release R14B01 (the patches still need work)

* Thu Nov 18 2010 Peter Lemenkov <lemenkov@gmail.com> - R14B-0.5
- Fixed building on EL-6

* Mon Nov 15 2010 Peter Lemenkov <lemenkov@gmail.com> - R14B-0.4
- No more dependent on erlang-rpm-macros sub-package

* Thu Nov 11 2010 Peter Lemenkov <lemenkov@gmail.com> - R14B-0.3
- Remove pre-built stuff

* Fri Nov  5 2010 Peter Lemenkov <lemenkov@gmail.com> - R14B-0.2
- Fixed doc-files and man-pages instalation for EL-5
- Temporarily (I hope) disabled emacs-related stuff in EL-5
- Disable erlang-rpm-macros subpackage for EL-5

* Wed Sep 29 2010 jkeating - R14B-0.1.1
- Rebuilt for gcc bug 634757

* Thu Sep 16 2010 Peter Lemenkov <lemenkov@gmail.com> - R14B-0.1
- R14B release

* Mon Aug  2 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - R14A-0.6
- Implement '--without doc' conditional for faster test builds (#618245).

* Fri Jul 30 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - R14A-0.5
- Properly hook up (X)Emacs erlang-mode (#491165)

* Mon Jul 26 2010 Hans Ulrich Niedermann <hun@n-dimensional.de> - R14A-0.4
- Spec file cleanups:
  - Avoid accidental %%rel increments by rpmdev-bumpspec.
  - Use %%global for our spec file macros.
  - Use macro for redundant directory names.
  - Whitespace cleanups (tabs vs. spaces).
  - Fix accidental macro usage in %%changelog.

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - R14A-0.3
- rebuilt against wxGTK-2.8.11-2

* Sat Jun 26 2010 Peter Lemenkov <lemenkov@gmail.com> - R14A-0.2
- Updated list of explicit requirements

* Fri Jun 18 2010 Peter Lemenkov <lemenkov@gmail.com> - R14A-0.1
- R14A release

* Sat May 15 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.12
- Moved dialyzer and typer executables from erts to appropriate rpms

* Fri May 14 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.11
- Do not mention nteventlog in os_mon.app, see rhbz #592251

* Thu May  6 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.10
- Disabled automatic requires/provides generation

* Wed Apr 28 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.9
- Added missing files, necessary for emacs (see rhbz #585349)
- Patches rebased

* Tue Apr 27 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.8
- Added missing BuildRequires libxslt (for building docs)
- Removed %%post script completely (resolves rhbz #586428)
- Since now both docs and man-pages are built from sources
- No need to manually create symlinks in %%{_bindir}

* Mon Apr 26 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.7
- Build with erlang-rpm-macros
- Man-files are packed with packages, they belong to

* Mon Apr 26 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.6
- Made erlang-rpm-macros as separate package
- Fix error while installing erlang-rpm-macros

* Wed Apr 21 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.5
- Use erlang rpm macros for adding provides/reqires
- All %%{_libdir}/erlang/lib/* items were splitted off from main package, which
  in turn becomes purely virtual now.
- Removing RPM_BUILD_ROOT from several installed files is no longer required

* Sat Apr 17 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.4
- Added missing Requires mesa-libGL{U} for wx module (rhbz #583287)
- Fix for buffer overflow in pcre module (rhbz #583288)
- Doc sub-package marked as noarch (partially resolves rhbz #491165)

* Fri Mar 26 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.3
- Added rpm-related stuff for auto-generating erlang dependencies in the future builds
- Since now *.yrl files are removed too.
- Removed unnecessary C and Java sources

* Fri Mar 26 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.2
- Do not remove all files from %%{_libdir}/erlang/lib/*/src - keep
  *.[yh]rl intact
- Fix permissions for megaco *.so objects
- Fix permissions for asn1 *.so objects

* Sat Feb 13 2010 Peter Lemenkov <lemenkov@gmail.com> - R13B-04.1
- New release R13B-04
- Since now we're using %%configure instead of ./configure
- Removed no longer needed fix for newer glibc version
- Dropped %%patch3 (applied upstream)
- Rebased patches
- Added BR fop for rebuilding of docs
- Use system-wide zlib instead of shipped one
- Dropped BR gd-devel
- Removed unneeded sources (should be fixed upstream)
- Fixed permission for wx driver (should be fixed upstream)

* Thu Oct 22 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - R13B-02-1
- Update to R13B-02 (patched for what's released as 02-1 by upstream)

* Tue Aug 25 2009 Tomas Mraz <tmraz@redhat.com> - R13B-01.2
- rebuilt with new openssl

* Mon Aug 10 2009 Gerard Milmeister <gemi@bluewin.ch> - R13B-01.1
- update to R13B01

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - R12B-6.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 21 2009 Debarshi Ray <rishi@fedoraproject.org> R12B-5.7
- Updated rpath patch.
- Fixed configure to respect $RPM_OPT_FLAGS.

* Sun Mar  1 2009 Gerard Milmeister <gemi@bluewin.ch> - R12B-5.6
- new release R12B-5
- link escript and dialyzer to %%{_bindir}

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - R12B-5.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Dennis Gilmore <dennis@ausil.us> - R12B-4.5
- fix sparc arches to compile

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - R12B-4.4
- rebuild with new openssl

* Sat Oct 25 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-4.1
- new release R12B-4

* Fri Sep  5 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-3.3
- fixed sslrpath patch

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> - R12B-3.2
- fix license tag

* Sun Jul  6 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-3.1
- new release R12B-3

* Thu Mar 27 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-1.1
- new release R12B-1

* Sat Feb 23 2008 Gerard Milmeister <gemi@bluewin.ch> - R12B-0.3
- disable strict aliasing optimization

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - R12B-0.2
- Autorebuild for GCC 4.3

* Sat Dec  8 2007 Gerard Milmeister <gemi@bluewin.ch> - R12B-0.1
- new release R12B-0

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org> - R11B-6
 - Rebuild for deps

* Sun Aug 19 2007 Gerard Milmeister <gemi@bluewin.ch> - R11B-5.3
- fix some permissions

* Sat Aug 18 2007 Gerard Milmeister <gemi@bluewin.ch> - R11B-5.2
- enable dynamic linking for ssl

* Sat Aug 18 2007 Gerard Milmeister <gemi@bluewin.ch> - R11B-5.1
- new release R11B-5

* Sat Mar 24 2007 Thomas Fitzsimmons <fitzsim@redhat.com> - R11B-2.4
- Require java-1.5.0-gcj-devel for build.

* Sun Dec 31 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-2.3
- remove buildroot from installed files

* Sat Dec 30 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-2.2
- added patch for compiling with glibc 2.5

* Sat Dec 30 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-2.1
- new version R11B-2

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-0.3
- Rebuild for FE6

* Wed Jul  5 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-0.2
- add BR m4

* Thu May 18 2006 Gerard Milmeister <gemi@bluewin.ch> - R11B-0.1
- new version R11B-0

* Wed May  3 2006 Gerard Milmeister <gemi@bluewin.ch> - R10B-10.3
- added patch for run_erl by Knut-Håvard Aksnes

* Mon Mar 13 2006 Gerard Milmeister <gemi@bluewin.ch> - R10B-10.1
- new version R10B-10

* Thu Dec 29 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-9.1
- New Version R10B-9

* Sat Oct 29 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-8.2
- updated rpath patch

* Sat Oct 29 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-8.1
- New Version R10B-8

* Sat Oct  1 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.4
- Added tk-devel and tcl-devel to buildreq
- Added tk to req

* Tue Sep  6 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.3
- Remove perl BuildRequires

* Tue Aug 30 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.2
- change /usr/lib to %%{_libdir}
- redirect output in %%post to /dev/null
- add unixODBC-devel to BuildRequires
- split doc off to erlang-doc package

* Sat Jun 25 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-6.1
- New Version R10B-6

* Sun Feb 13 2005 Gerard Milmeister <gemi@bluewin.ch> - R10B-3.1
- New Version R10B-3

* Mon Dec 27 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:R10B-2-0.fdr.1
- New Version R10B-2

* Wed Oct  6 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:R10B-0.fdr.1
- New Version R10B

* Thu Oct 16 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:R9B-1.fdr.1
- First Fedora release
