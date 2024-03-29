Summary:	Tux Math - educational math game
Summary(pl.UTF-8):	Tux Math - gra edukacyjna z zakresu matematyki
Name:		tuxmath
Version:	2001.09.07
%define		_subver	0102
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-%{_subver}.tar.gz
# Source0-md5:	435ba5d937106ca8b7da46c1a95a0d8c
Source1:	%{name}.desktop
Patch0:		%{name}-Makefile.patch
URL:		http://www.newbreedsoftware.com/tuxmath/
BuildRequires:	SDL_image-devel >= 1.2.2
BuildRequires:	SDL_mixer-devel >= 1.2.4
BuildRequires:	SDL_ttf-devel >= 2.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An educational math tutorial game starring Tux, the Linux Penguin.

%description -l pl.UTF-8
Gra edukacyjna, w której występuje linuksowy pingwinek - Tux.

%prep
%setup -q -n %{name}
%patch0 -p0

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir},%{_datadir}/%{name}}

%{__make} _prefix=$RPM_BUILD_ROOT%{_prefix} install

install data/images/.xvpics/icon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

rm -rf $(find $RPM_BUILD_ROOT -type d -name CVS)
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/images/.xvpics

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_datadir}/%{name}
