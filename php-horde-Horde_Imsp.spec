# TODO
# - system locale dir
%define		status		stable
%define		pearname	Horde_Imsp
Summary:	%{pearname} - IMSP API
Name:		php-horde-Horde_Imsp
Version:	1.0.6
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	97d6bd47a71829cbfc78b51b6d73a0ef
URL:		https://github.com/horde/horde/tree/master/framework/Imsp/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an API into an IMSP server for address books and options.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Imsp
%{php_pear_dir}/data/Horde_Imsp
