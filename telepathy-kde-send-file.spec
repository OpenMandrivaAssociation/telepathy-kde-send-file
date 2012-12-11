%define srcname ktp-send-file

Summary:	File Manager plugin to launch a file transfer job with a specified contact
Name:		telepathy-kde-send-file
Version:	0.5.1
Release:	1
Url:		https://projects.kde.org/projects/playground/network/telepathy/telepathy-send-file
Source0:	ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%srcname-%version.tar.bz2
License:	GPLv2+
Group:		Networking/Instant messaging
BuildRequires:	telepathy-kde-common-internals-devel >= %{version}
Requires:	telepathy-kde-common-internals-core


%description
A File manager plugin to launch a file transfer job with a specified contact.

%files -f ktp-send-file.lang
%{_kde_bindir}/ktp-send-file
%{_kde_services}/ServiceMenus/ktp-send-file.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %srcname-%version
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang ktp-send-file
