%include	/usr/lib/rpm/macros.perl
Summary:	PostgreSQL table checker and dumper
Summary(pl.UTF-8):	Narzędzie do sprawdzania baz systemu PostgreSQL
Name:		pgfsck
Version:	0.14
Release:	0.1
License:	BSD
Group:		Applications/Databases
Source0:	http://svana.org/kleptog/pgsql/%{name}-%{version}.tar.gz
# Source0-md5:	27440e1a30323cf9d91fefe8711d3337
URL:		http://svana.org/kleptog/pgsql/pgfsck.html
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostgreSQL table checker and dumper.

%description -l pl.UTF-8
Narzędzie do sprawdzania baz systemu PostgreSQL.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}

install -D pgfsck $RPM_BUILD_ROOT%{_sbindir}/pgfsck
install *.pm $RPM_BUILD_ROOT%{perl_vendorlib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{perl_vendorlib}/*
