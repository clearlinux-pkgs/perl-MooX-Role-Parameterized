#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MooX-Role-Parameterized
Version  : 0.082
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/P/PA/PACMAN/MooX-Role-Parameterized-0.082.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PA/PACMAN/MooX-Role-Parameterized-0.082.tar.gz
Summary  : 'MooX::Role::Parameterized - roles with composition parameters'
Group    : Development/Tools
License  : MIT
Requires: perl-MooX-Role-Parameterized-license = %{version}-%{release}
Requires: perl-MooX-Role-Parameterized-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Method::Modifiers)
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(Exporter::Tiny)
BuildRequires : perl(List::MoreUtils)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Moo)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)

%description
This archive contains the distribution MooX-Role-Parameterized,
version 0.082:
MooX::Role::Parameterized - roles with composition parameters

%package dev
Summary: dev components for the perl-MooX-Role-Parameterized package.
Group: Development
Provides: perl-MooX-Role-Parameterized-devel = %{version}-%{release}
Requires: perl-MooX-Role-Parameterized = %{version}-%{release}

%description dev
dev components for the perl-MooX-Role-Parameterized package.


%package license
Summary: license components for the perl-MooX-Role-Parameterized package.
Group: Default

%description license
license components for the perl-MooX-Role-Parameterized package.


%package perl
Summary: perl components for the perl-MooX-Role-Parameterized package.
Group: Default
Requires: perl-MooX-Role-Parameterized = %{version}-%{release}

%description perl
perl components for the perl-MooX-Role-Parameterized package.


%prep
%setup -q -n MooX-Role-Parameterized-0.082
cd %{_builddir}/MooX-Role-Parameterized-0.082

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MooX-Role-Parameterized
cp %{_builddir}/MooX-Role-Parameterized-0.082/LICENSE %{buildroot}/usr/share/package-licenses/perl-MooX-Role-Parameterized/80f2bd287ec01b4bd44170a77b73eb180c53341d
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MooX::Role::Parameterized.3
/usr/share/man/man3/MooX::Role::Parameterized::Proxy.3
/usr/share/man/man3/MooX::Role::Parameterized::With.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MooX-Role-Parameterized/80f2bd287ec01b4bd44170a77b73eb180c53341d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/MooX/Role/Parameterized.pm
/usr/lib/perl5/vendor_perl/5.34.0/MooX/Role/Parameterized/Proxy.pm
/usr/lib/perl5/vendor_perl/5.34.0/MooX/Role/Parameterized/With.pm
