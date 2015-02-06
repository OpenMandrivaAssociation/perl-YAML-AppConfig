%define upstream_name	 YAML-AppConfig
%define upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Manage configuration files with YAML and variable reference
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.bz2
Patch:		YAML-AppConfig-0.16-fix-warning.patch

BuildRequires:	perl-devel
BuildRequires:	perl-YAML-parser
Requires:	perl-YAML-parser
BuildArch:	noarch

%description
YAML::AppConfig extends the work done in Config::YAML and YAML::ConfigFile to
allow more flexiable configuration files.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{_mandir}/*/*
%{perl_vendorlib}/YAML


%changelog
* Mon Feb 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.160.0-3mdv2011.0
+ Revision: 636719
- patch: fix deprecated usage of UNIVERSAL::isa as a function

* Thu Sep 23 2010 Funda Wang <fwang@mandriva.org> 0.160.0-2mdv2011.0
+ Revision: 580731
- rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 401809
- rebuild using %%perl_convert_version
- fixed license field

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-8mdv2009.1
+ Revision: 324627
- requires any perl YAML parser
- fix dependencies

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.16-6mdv2009.0
+ Revision: 258886
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.16-5mdv2009.0
+ Revision: 246793
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-3mdv2008.1
+ Revision: 133737
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-2mdv2007.0
- buildrequires perl(YAML)

* Tue Oct 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2007.0
- first mdv release

