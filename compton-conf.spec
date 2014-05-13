%define		qtver		4.8.5

Summary:	compton-conf
Name:		compton-conf
Version:	0.1.0
Release:	0.1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://lxqt.org/downloads/compton-conf/0.1.0/%{name}-%{version}.tar.xz
# Source0-md5:	d50ff2a705d7c5dd1074bb187630ab98
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
%setup -q -c %{name}-%{version}

%build
install -d build
cd build
%cmake \
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
