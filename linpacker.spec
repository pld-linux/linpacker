Summary:	linpacker is a scientific tool for studying rectangle packings
Summary(pl):	Naukowe narzêdzie do studiowania pakowania wiek±tów
Name:		linpacker
Version:	0.5.3
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://freehackers.org/~tnagy/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	8dda9b7b34a3bef329027a067869e574
URL:		http://freehackers.org/~tnagy/linpacker/
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
linpacker is a scientific tool for studying rectangle packings.

%description -l pl
Naukowe narzêdzie do studiowania pakowania wiek±tów.

%prep
%setup -q

%build
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
