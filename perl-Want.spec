#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Want
Summary:	Want - A generalisation of "wantarray"
Summary(pl):	Want - Generalizacja funkcji wantarray()
Name:		perl-Want
Version:	0.05
Release:	2
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/R/RO/ROBIN/%{pdir}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
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

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/Want
%{perl_vendorarch}/auto/Want/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Want/*.so
%{_mandir}/man3/*
