#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pexpect
Version  : 4.0.1
Release  : 16
URL      : https://pypi.python.org/packages/source/p/pexpect/pexpect-4.0.1.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pexpect/pexpect-4.0.1.tar.gz
Summary  : Pexpect allows easy control of interactive console applications.
Group    : Development/Tools
License  : ISC
Requires: pexpect-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
The best way to run these tests is from the directory above this one. Run:
py.test

%package python
Summary: python components for the pexpect package.
Group: Default

%description python
python components for the pexpect package.


%prep
%setup -q -n pexpect-4.0.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
