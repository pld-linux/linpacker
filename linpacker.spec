Summary:	linpacker is a scientific tool for studying rectangle packings
Summary(pl):	Naukowe narzêdzie do studiowania pakowania wielok±tów
Name:		linpacker
Version:	0.5.6
Release:	1
%ifarch %{ix86}
License:	GPL with BSD-licensed, closed-source plugins
%else
License:	GPL
%endif
Group:		Applications/Math
Source0:	http://freehackers.org/~tnagy/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	ea4175629d728b634f8b4f4fa2ceac91
Patch0:		%{name}-libdir.patch
Patch1:		%{name}-desktop.patch
URL:		http://freehackers.org/~tnagy/linpacker/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	qt-devel >= 3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
linpacker is a scientific tool for studying rectangle packings.

%description -l pl
Naukowe narzêdzie do studiowania pakowania wielok±tów.

%prep
%setup -q -n %{name}-%(echo %{version}|cut -f -3 -d .)
%patch0 -p0
%patch1 -p1

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

# BSD license, sources not provided, only x86 binaries
%ifnarch %{ix86}
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins
%endif
# compiled for i586
%ifarch i386 i486
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*2DBP1*
%endif

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
