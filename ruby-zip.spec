%define rname zip
%define name  ruby-%{rname}
%define oname rubyzip

%define version 0.9.1
%define release %mkrel 4

Summary: Ruby module for reading and writing zip files
Name: %name
Version: %version
Release: %release
License: BSD-like
Group: Development/Ruby
URL: http://rubyzip.sourceforge.net
Source0: %{oname}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: ruby-devel ruby-rake
Buildarch: noarch
Provides: %{oname}

%description
Ruby module for reading and writing zip files

%prep
%setup -q -n %{oname}-%{version}
sed -i -e 's£CONFIG\[£"%buildroot"+CONFIG\[£' install.rb
sed -i "s/\r//" samples/write_simple.rb

%build
cd test
ruby alltests.rb

%clean
rm -rf %buildroot

%install
rm -rf %buildroot
ruby install.rb

%files
%defattr(-,root,root)
%{ruby_sitelibdir}/%{rname}
%doc ChangeLog NEWS README TODO samples/ 

