#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Want
Summary:	Want - a generalisation of "wantarray"
Summary(pl):	Want - uogólnienie funkcji wantarray()
Name:		perl-Want
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RO/ROBIN/%{pdir}-%{version}.tar.gz
# Source0-md5:	72f9a5b7d9300859c23a61a31c21f91b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(v5.6)'

%description
This module generalises the mechanism of the wantarray function, allowing
a function to determine in some detail how its return value is going to
be immediately used.

%description -l pl
Ten modu³ generalizuje mechanizm funkcji wantarray, pozwalaj±c funkcjom
na okre¶lenie niektórych szczegó³ów tego, w jaki sposób u¿ywane bêd±
zwracane przez nie warto¶ci.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/Want
%{perl_vendorarch}/auto/Want/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Want/*.so
%{_mandir}/man3/*
