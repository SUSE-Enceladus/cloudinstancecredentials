#
# spec file for package python3-cloudinstancecredentials
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define upstream_name cloudinstancecredentials

Name:           python3-cloudinstancecredentials
Version:        0.2.0
Release:        0
Summary:        authorization utilities for public cloud
License:        GPL-3.0+
Url:            https://github.com/SUSE-Enceladus/cloudinstancecredentials
Source0:        %{upstream_name}-%{version}.tar.bz2
Requires:       python3
Requires:       python3-requests
BuildRequires:  python3-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch


%description
Command line tools for setting authorization credentials based on metadata
present in a public cloud VM instance.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/set-http-basic-credentials %{buildroot}%{_sbindir}/set-http-basic-credentials
mv %{buildroot}%{_bindir}/cloudinstancecredentials-config %{buildroot}%{_sbindir}/cloudinstancecredentials-config
mkdir -p %{buildroot}%{_unitdir}
install -m 444 set-http-basic-credentials.service %{buildroot}%{_unitdir}
install -m 444 cloudinstancecredentials-config.service %{buildroot}%{_unitdir}

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%dir %{python3_sitelib}/cloudinstancecredentials
%{python3_sitelib}/*
%{_sbindir}/set-http-basic-credentials
%{_sbindir}/cloudinstancecredentials-config
%{_unitdir}/set-http-basic-credentials.service
%{_unitdir}/cloudinstancecredentials-config.service

%changelog
