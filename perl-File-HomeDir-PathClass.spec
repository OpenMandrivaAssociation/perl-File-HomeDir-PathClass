%define upstream_name    File-HomeDir-PathClass
%define upstream_version 1.112060

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 1.112060
Release:    3

Summary:    File::HomeDir returning Path::Class objects
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/File-HomeDir-PathClass-1.112060.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build)
BuildArch: noarch


%description
This module is just a wrapper around the File::HomeDir manpage methods,
transforming their return value to the Path::Class manpage objects. This
allows for easier usage of the value.

Refer to the File::HomeDir#METHODS manpage for a list of which functions
are supported.

'File::HomeDir::PathClass' supports both original the File::HomeDir manpage
interfaces.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*

%changelog
* Fri Jul 08 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.101.611-1mdv2011
+ Revision: 689332
- import perl-File-HomeDir-PathClass


