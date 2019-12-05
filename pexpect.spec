#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pexpect
Version  : 4.7.0
Release  : 58
URL      : https://files.pythonhosted.org/packages/1c/b1/362a0d4235496cb42c33d1d8732b5e2c607b0129ad5fdd76f5a583b9fcb3/pexpect-4.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/1c/b1/362a0d4235496cb42c33d1d8732b5e2c607b0129ad5fdd76f5a583b9fcb3/pexpect-4.7.0.tar.gz
Summary  : Pexpect allows easy control of interactive console applications.
Group    : Development/Tools
License  : ISC
Requires: pexpect-license = %{version}-%{release}
Requires: pexpect-python = %{version}-%{release}
Requires: pexpect-python3 = %{version}-%{release}
Requires: ptyprocess
BuildRequires : buildreq-distutils3
BuildRequires : ptyprocess

%description
This directory contains scripts that give examples of using Pexpect.
hive.py
This script creates SSH connections to a list of hosts that
you provide. Then you are given a command line prompt. Each
shell command that you enter is sent to all the hosts. The
response from each host is collected and printed. For example,
you could connect to a dozen different machines and reboot
them all at once.

%package license
Summary: license components for the pexpect package.
Group: Default

%description license
license components for the pexpect package.


%package python
Summary: python components for the pexpect package.
Group: Default
Requires: pexpect-python3 = %{version}-%{release}

%description python
python components for the pexpect package.


%package python3
Summary: python3 components for the pexpect package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pexpect package.


%prep
%setup -q -n pexpect-4.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554647756
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pexpect
cp LICENSE %{buildroot}/usr/share/package-licenses/pexpect/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pexpect/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
