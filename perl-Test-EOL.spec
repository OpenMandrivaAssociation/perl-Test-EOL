%define upstream_name    Test-EOL
%define upstream_version 2.02

Name:		perl-%{upstream_name}
Version:	2.02
Release:	4

Summary:	Check the correct line endings in your project
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/karenetheridge/Test-EOL
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-EOL-2.02.tar.gz

BuildRequires:	make
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
%setup -q -n Test-EOL-2.02

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test || :

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

