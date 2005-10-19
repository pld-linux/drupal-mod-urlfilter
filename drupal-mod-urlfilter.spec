%define		modname urlfilter
Summary:	Drupal URL Filter Module
Summary(pl):	Modu³ URL Filter dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	bd7d7cc306a54d7f463dba53334a54cc
URL:		http://drupal.org/project/urlfilter
BuildRequires:	rpmbuild(macros) >= 1.194
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules
%define		_podir		%{_drupaldir}/po/%{modname}

%description
This is a simple filter module. It automatically converts URLs (http,
ftp, email, ...) into hyperlinks.

%description -l pl
To jest prosty modu³ filtra. Automatycznie przekszta³ca URL-e (http,
ftp, email...) na hiper³±cza.

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_moddir},%{_podir}}

install *.module $RPM_BUILD_ROOT%{_moddir}
cp -a po/*.po $RPM_BUILD_ROOT%{_podir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
%banner -e %{name} <<EOF
If you want to use localization, then you need to upload .po files
from %{_podir} via drupal locatization admin.

EOF
fi

%files
%defattr(644,root,root,755)
%doc *.txt po/*.pot
%{_moddir}/*.module
%{_podir}
