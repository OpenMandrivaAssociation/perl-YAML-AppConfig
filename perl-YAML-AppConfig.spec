%define upstream_name	 YAML-AppConfig
%define upstream_version 0.16

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 3

Summary: 	Manage configuration files with YAML and variable reference
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.bz2
Patch:          YAML-AppConfig-0.16-fix-warning.patch

BuildRequires:	perl-YAML-parser
Requires:	    perl-YAML-parser
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
YAML::AppConfig extends the work done in Config::YAML and YAML::ConfigFile to
allow more flexiable configuration files.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_mandir}/*/*
%{perl_vendorlib}/YAML
