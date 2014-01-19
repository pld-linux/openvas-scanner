
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs

Summary:	Open Vulnerability Assessment System scanner
Name:		openvas-scanner
Version:	3.4.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://wald.intevation.org/frs/download.php/1307/%{name}-%{version}.tar.gz
# Source0-md5:	66c8d5baf4f5a070afcff04b779e8db7
URL:		http://www.openvas.org/
BuildRequires:	cmake
BuildRequires:	glib2-devel >= 2.16
BuildRequires:	gnutls-devel > 2.8
BuildRequires:	openvas-libraries-devel >= 6.0.0
BuildRequires:	pkgconfig
%if %{with apidocs}
BuildRequires:	doxygen
#BuildRequires:	sqlfairy
#BuildRequires:	xmltoman
%endif
BuildConflicts:	openvas-libraries-devel >= 7.0
Requires:	openvas-common >= 6.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the scanner module for the Open Vulnerability Assessment
System (OpenVAS).

The Open Vulnerability Assessment System (OpenVAS) is a framework of
several services and tools offering a comprehensive and powerful
vulnerability scanning and vulnerability management solution.

%package apidocs
Summary:	OpenVAS scanner API documentation
Summary(pl.UTF-8):	Dokumentacja API skanera OpenVAS
Group:		Documentation

%description apidocs
OpenVAS scanner API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API skanera OpenVAS.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DLOCALSTATEDIR=/var \
	..
%{__make}

%if %{with apidocs}
%{__make} doc
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES ChangeLog README COPYING INSTALL
%doc doc/{kb_entries.txt,nbe_file_format.txt,nsr_file_format.txt}
%dir %{_sysconfdir}/openvas/gnupg
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*.8*
