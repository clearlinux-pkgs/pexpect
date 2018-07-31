#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pexpect
Version  : 4.6.0
Release  : 50
URL      : https://files.pythonhosted.org/packages/89/43/07d07654ee3e25235d8cea4164cdee0ec39d1fda8e9203156ebe403ffda4/pexpect-4.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/89/43/07d07654ee3e25235d8cea4164cdee0ec39d1fda8e9203156ebe403ffda4/pexpect-4.6.0.tar.gz
Summary  : Pexpect allows easy control of interactive console applications.
Group    : Development/Tools
License  : ISC
Requires: pexpect-python3
Requires: pexpect-license
Requires: pexpect-python
Requires: ptyprocess
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : ptyprocess

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


%package license
Summary: license components for the pexpect package.
Group: Default

%description license
license components for the pexpect package.


%package python
Summary: python components for the pexpect package.
Group: Default
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
%setup -q -n pexpect-4.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533052551
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1533052551
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pexpect
cp LICENSE %{buildroot}/usr/share/doc/pexpect/LICENSE
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

%files license
%defattr(-,root,root,-)
/usr/share/doc/pexpect/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
