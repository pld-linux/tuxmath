#
# TODO:
#
# description, summary, check comment at .desktop file
#
Summary:	Tux Math
Summary(pl):	Tux Math
Name:		tuxmath
Version:	2001.09.07
%define		_subver	0102
Release:	0.9
License:	GPL
Group:		X11/Applications/Games
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}-%{_subver}.tar.gz
URL:		http://www.newbreedsoftware.com/tuxmath/
Source1:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
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
%patch0 -p0

%build
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/pixmaps,%{_applnkdir}/Games,%{_datadir}/%{name}}
%{__make} _prefix=$RPM_BUILD_ROOT%{_prefix} install
cp data/images/.xvpics/icon.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{name}.png
cp %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/

rm -rf $(find $RPM_BUILD_ROOT -type d -name CVS)
rm -rf $RPM_BUILD_ROOT/%{_datadir}/%{name}/images/.xvpics/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/
%attr(755,root,root)%{_bindir}
%{_applnkdir}
%{_datadir}/pixmaps
%{_datadir}/%{name}
