Summary: 	axe theme
Name:    	xfwm4-axe-theme
Version: 	1.0.0
Release: 	1
Source0: 	73291-axe.tar.gz

License: 	GPL
Group: 		Graphical desktop/Xfce
URL:   	   	http://xfce-look.org/content/show.php/axe?content=73291
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch

%description
A xfwm4 theme axe

%prep
%setup -c axe_theme
%build

%install
%__install -d %{buildroot}%{_datadir}/themes/
%__cp -rf ./* %{buildroot}%{_datadir}/themes/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/themes/*


%changelog
* Fri Jul 28 2013 Mank <Mank1@seznam.cz> 1.0.0-1
- Init spec

