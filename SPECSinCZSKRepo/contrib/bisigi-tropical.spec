%define name gnome-bisigi-tropical-theme
%define version 1.7.1
%define release %mkrel 1

%define themesdir %{_datadir}/themes
%define iconsdir %{_datadir}/icons
%define wallpapersdir %{_datadir}/backgrounds
%define wallpaperspropdir %{_datadir}/gnome-background-properties
%define docsdir %{_docdir}/%{name}
%define emeralddir %{_datadir}/emerald/themes/tropical


Summary: 	Bisigi theme
Name:    	%{name}
Version: 	%{version}
Release: 	%{release}
Source1: 	tropical-theme.tar.bz2

License: 	GPL
Group: 		Graphical desktop/GNOME
URL:   	   	http://www.bisigi-project.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
Requires:	murrine emerald

%description
Tropical theme contains a full theme for GNOME based system.
It includes the following components:
   * "Tropical" wallpapers
   * GTK+ theme
   * Metacity theme
   * Tropical Icons set
   * Tropical Emerald theme

%prep

tar --bzip2 -xf %{SOURCE1}

%install

%__rm -rf %{buildroot}
%__install -d %{buildroot}%{themesdir}
%__install -d %{buildroot}%{iconsdir}
%__install -d %{buildroot}%{wallpapersdir}
%__install -d %{buildroot}%{wallpaperspropdir}
%__install -d %{buildroot}%{docsdir}
%__install -d %{buildroot}%{emeralddir}

cd tropical-theme/Wallpaper
%__cp -rf *.jpg %{buildroot}%{wallpapersdir}
%__cp -rf *.xml %{buildroot}%{wallpaperspropdir}
cd ..
%__cp -rf COPYING %{buildroot}%{docsdir}
%__cp -rf credits %{buildroot}%{docsdir}
cd Gtk
%__cp -rf ./* %{buildroot}%{themesdir}
cd ..
cd Emerald
%__cp -rf *.emerald %{buildroot}%{emeralddir}
cd ..
cd Icons
%__cp -rf ./* %{buildroot}%{iconsdir}
cd ..
cd ..


%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{docsdir}/* 
%{themesdir}/*
%{iconsdir}/*
%{wallpapersdir}/*
%{wallpaperspropdir}/*
%{emeralddir}/*


%changelog
* Fri Feb 11 2011 Cristobal Lopez <lopeztobal@gmail.com> 1.7.1-1mib2010.2
- Update.

* Fri Aug 20 2010 Cristobal Lopez <lopeztobal@gmail.com> 1.6.3-1mib2010.1
- Update.

* Sat Jul 10 2010 Cristobal Lopez <lopeztobal@gmail.com> 1.6.2-1mib2010.1
- Update.