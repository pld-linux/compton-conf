%define		qtver		4.8.5

Summary:	compton-conf
Name:		compton-conf
Version:	0.2.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://downloads.lxqt.org/compton-conf/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	b40265ae0b2a4d40b203046c57a0c08e
URL:		http://www.lxqt.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	libconfig-devel
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
compton-conf

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DPULL_TRANSLATIONS:BOOL=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/compton-conf
%{_desktopdir}/compton-conf.desktop
%dir %{_datadir}/compton-conf
%{_datadir}/compton-conf/compton.conf.example
