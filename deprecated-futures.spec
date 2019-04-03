#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : deprecated-futures
Version  : 3.2.0
Release  : 46
URL      : https://files.pythonhosted.org/packages/1f/9e/7b2ff7e965fc654592269f2906ade1c7d705f1bf25b7d469fa153f7d19eb/futures-3.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/1f/9e/7b2ff7e965fc654592269f2906ade1c7d705f1bf25b7d469fa153f7d19eb/futures-3.2.0.tar.gz
Summary  : Backport of the concurrent.futures package from Python 3
Group    : Development/Tools
License  : Python-2.0
Requires: deprecated-futures-license = %{version}-%{release}
Requires: deprecated-futures-python = %{version}-%{release}
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3

%description
.. image:: https://travis-ci.org/agronholm/pythonfutures.svg?branch=master
:target: https://travis-ci.org/agronholm/pythonfutures
:alt: Build Status

%package legacypython
Summary: legacypython components for the deprecated-futures package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-futures package.


%package license
Summary: license components for the deprecated-futures package.
Group: Default

%description license
license components for the deprecated-futures package.


%package python
Summary: python components for the deprecated-futures package.
Group: Default

%description python
python components for the deprecated-futures package.


%prep
%setup -q -n futures-3.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554320265
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 test_futures.py
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-futures
cp LICENSE %{buildroot}/usr/share/package-licenses/deprecated-futures/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-futures/LICENSE

%files python
%defattr(-,root,root,-)
