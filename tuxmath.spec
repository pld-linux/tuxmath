Summary:	Tux Math
Summary(pl):	Tux Math
Name:		tuxmath
Version:	2001.09.07
%define		_subver	0102
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}-%{_subver}.tar.gz
URL:		http://www.newbreedsoftware.com/tuxmath/
BuildRequires:	SDL_image-devel >= 1.2.2
BuildRequires:	SDL_ttf-devel >= 2.0.5
BuildRequires:	SDL_mixer-devel >= 1.2.4
#Requires:
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix /usr/X11R6

%description

%description -l pl

%prep
%setup -q -n %{name}
#%patch0 -p0

%build
%{__make} CC=gcc \
PREFIX=%{_prefix}/ \
CONFDIR=%{_sysconfdir}/tuxpaint/ \
DATA_PREFIX=%{_datadir}/tuxpaint/ \
DOC_PREFIX=%{_datadir}/doc/ \
MAN_PREFIX=%{_mandir}/ \
ICON_PREFIX=%{_datadir}/pixmaps/ \
X11_ICON_PREFIX=%{_datadir}/pixmaps/ \
GNOME_PREFIX=%{_applnkdir}/Graphics/ \
KDE_PREFIX=%{_applnkdir}/Graphics/ \
LOCALE_PREFIX=%{_datadir}/locale/ \
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/%{name},%{_datadir}/pixmaps,%{_applnkdir}/Graphics,%{_datadir}/%{name}/stamps}
%{__make} _prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/
%attr(755,root,root)%{_bindir}
%{_sysconfdir}/%{name}
%{_applnkdir}
%{_datadir}/pixmaps
%{_datadir}/locale
%{_datadir}/%{name}/brushes
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/images
%{_datadir}/%{name}/sounds
