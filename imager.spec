Name:           imager
Version:        0.1
Release:        alt1
Summary:        A simple image utility tool
Group:          Graphics
License:        MIT
URL:            https://github.com/vasthecat/imager
Source0:        imager-0.1.tar
 
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  libSDL2-devel
BuildRequires:  libSDL2_image-devel
 
Requires:       libcurl
Requires:       SDL2
Requires:       SDL2_image
 
%description
A simple image utility tool from GitHub.
 
%prep
tar -xf %{SOURCE0}
 
%build
cd imager-0.1
mkdir -p build
cd build
cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix}
make %{?_smp_mflags}
 
%install
cd imager-0.1/build
make install DESTDIR=%{buildroot}
 
%files
%{_bindir}/imager
%{_datadir}/applications/imager.desktop
 
%changelog
* Tue Feb 03 2026 Andrew Guschin <guschin@altlinux.org> 0.1-alt1
- Initial package for ALT Linux.
