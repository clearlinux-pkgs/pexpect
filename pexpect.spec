#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pexpect
Version  : 4.3.1
Release  : 34
URL      : https://pypi.python.org/packages/14/05/47c8bca66390c9b18c91f6152db4b74eb850382e8e13aa2f06dfb3036466/pexpect-4.3.1.tar.gz
Source0  : https://pypi.python.org/packages/14/05/47c8bca66390c9b18c91f6152db4b74eb850382e8e13aa2f06dfb3036466/pexpect-4.3.1.tar.gz
Summary  : Pexpect allows easy control of interactive console applications.
Group    : Development/Tools
License  : ISC
Requires: pexpect-legacypython
Requires: pexpect-python3
Requires: pexpect-python
Requires: ptyprocess
BuildRequires : pbr
BuildRequires : pip
BuildRequires : ptyprocess
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Pexpect is a pure Python module for spawning child applications; controlling
        them; and responding to expected patterns in their output. Pexpect works like
        Don Libes' Expect. Pexpect allows your script to spawn a child application and
        control it as if a human were typing commands.
        
        Pexpect can be used for automating interactive applications such as ssh, ftp,
        passwd, telnet, etc. It can be used to a automate setup scripts for duplicating
        software package installations on different servers. It can be used for
        automated software testing. Pexpect is in the spirit of Don Libes' Expect, but
        Pexpect is pure Python.
        
        The main features of Pexpect require the pty module in the Python standard
        library, which is only available on Unix-like systems. Some featuresâwaiting
        for patterns from file descriptors or subprocessesâare also available on
        Windows.

%package legacypython
Summary: legacypython components for the pexpect package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pexpect package.


%package python
Summary: python components for the pexpect package.
Group: Default
Requires: pexpect-legacypython
Requires: pexpect-python3

%description python
python components for the pexpect package.


%package python3
Summary: python3 components for the pexpect package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pexpect package.


%prep
%setup -q -n pexpect-4.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513086275
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1513086275
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
