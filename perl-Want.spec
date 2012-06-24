#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Want
Summary:	Want - a generalisation of "wantarray"
Summary(pl):	Want - uog�lnienie funkcji wantarray()
Name:		perl-Want
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/R/RO/ROBIN/%{pdir}-%{version}.tar.gz
# Source0-md5:	55dda301deb9bd5748c342eef7c1ec08
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(v5.6)'

%description
This module generalises the mechanism of the wantarray function, allowing
a function to determine in some detail how its return value is going to
be immediately used.

%description -l pl
Ten modu� generalizuje mechanizm funkcji wantarray, pozwalaj�c funkcjom
na okre�lenie niekt�rych szczeg��w tego, w jaki spos�b u�ywane b�d�
zwracane przez nie warto�ci.

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
