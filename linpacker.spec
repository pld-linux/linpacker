Summary:	linpacker is a scientific tool for studying rectangle packings
Summary(pl):	Naukowe narzêdzie do studiowania pakowania wielok±tów
Name:		linpacker
Version:	0.5.4.1
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://freehackers.org/~tnagy/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	ad64b4b8edede6605d7e51f839efe180
# Source0-size:	470897
URL:		http://freehackers.org/~tnagy/linpacker/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
linpacker is a scientific tool for studying rectangle packings.

%description -l pl
Naukowe narzêdzie do studiowania pakowania wielok±tów.

%prep
%setup -q -n %{name}-%(echo %{version}|cut -f -3 -d .)

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f Makefile.cvs
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D $RPM_BUILD_ROOT%{_datadir}/applications/kde/%{name}.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/%{name}
%{_datadir}/config.kcfg/%{name}*
%{_iconsdir}/*/*/*/%{name}.png
%{_desktopdir}/%{name}.desktop
