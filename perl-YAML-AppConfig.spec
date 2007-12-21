%define module	YAML-AppConfig
%define name	perl-%{module}
%define version	0.16
%define release	%mkrel 3

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Manage configuration files with YAML and variable reference
License: 	GPL or Artistic
Group: 		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/WWW/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(YAML)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
YAML::AppConfig extends the work done in Config::YAML and YAML::ConfigFile to
allow more flexiable configuration files.


%prep
%setup -q -n %{module}-%{version}

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

