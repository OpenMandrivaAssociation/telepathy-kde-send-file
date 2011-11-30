%define rel 1

Summary:	File Manager plugin to launch a file transfer job with a specified contact
Name:		telepathy-kde-send-file
Version:	0.2.0
Release:	%mkrel %{rel} 
Url:		https://projects.kde.org/projects/playground/network/telepathy/telepathy-send-file
Source0:	ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%name-%version.tar.bz2
Patch0:         telepathy-kde-send-file-fix-desktop-file.patch
License:	GPLv2+
Group:		Graphical desktop/KDE
BuildRequires:	kdelibs4-devel
BuildRequires:	telepathy-qt4-devel


%description
A File manager plugin to launch a file transfer job with a specified contact

%files -f %{name}.lang
%{_kde_bindir}/telepathy-kde-send-file
%{_kde_applicationsdir}/telepathy-kde-send-file.desktop
#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang %name


