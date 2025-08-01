#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Want
Summary:	Want - a generalisation of "wantarray"
Summary(pl.UTF-8):	Want - uogólnienie funkcji wantarray()
Name:		perl-Want
Version:	0.29
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RO/ROBIN/%{pdir}-%{version}.tar.gz
# Source0-md5:	33b2dae5db59781b9a0434fa1db04aab
URL:		http://search.cpan.org/dist/Want/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(v5.6)'

%description
This module generalises the mechanism of the wantarray function,
allowing a function to determine in some detail how its return value
is going to be immediately used.

%description -l pl.UTF-8
Ten moduł generalizuje mechanizm funkcji wantarray, pozwalając
funkcjom na określenie niektórych szczegółów tego, w jaki sposób
używane będą zwracane przez nie wartości.

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
%attr(755,root,root) %{perl_vendorarch}/auto/Want/*.so
%{_mandir}/man3/*
