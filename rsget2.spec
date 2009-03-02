#
%define		snap	10061
%include        /usr/lib/rpm/macros.perl
Summary:	Command line downloader for RapidShare-like services
Name:		rsget2
Version:	0
Release:	0.%{snap}.0.1
License:	GPL v2+
Group:		Applications
Source0:	http://svn.pld-linux.org/svn/toys/fun/rsget.pl
# Source0-md5:	a6bf82e9c225cceda61b071c573ff785
URL:		http://svn.pld-linux.org/svn/toys/fun/
BuildRequires:	rpm-perlprov
Requires:	netpbm-progs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line downloader for RapidShare-like services.

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install %SOURCE0 $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
