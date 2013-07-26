%define upstream_name    Test-EOL
%define upstream_version 1.5

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.5
Release:	1

Summary:	Check the correct line endings in your project
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-EOL-1.5.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(vars)
BuildArch:	noarch

%description
This module scans your project/distribution for any perl files (scripts,
modules, etc) for the presence of windows line endings.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.900.0-2mdv2011.0
+ Revision: 656824
- rebuild for updated spec-helper

* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.900.0-1mdv2011.0
+ Revision: 572786
- import perl-Test-EOL


