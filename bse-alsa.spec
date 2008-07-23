%define	version	0.7.1

Summary:	ALSA plugin for BSE (Bedevilled Sound Engine)
Name:		bse-alsa
Version:	%{version}
Release:	%mkrel 5
License:	GPL
Group:		Sound
URL:		http://beast.gtk.org/
Source0:	ftp://beast.gtk.org/pub/beast/v0.7/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	beast-devel
BuildRequires:	alsa-lib-devel

%description
This is ALSA plugin for BSE (Bedevilled Sound Engine). It provides
ALSA PCM driver and MIDI driver for BSE.


%prep
%setup -q

%build
%configure2_5x
%make


%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/bse/v*/drivers


