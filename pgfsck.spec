
%include /usr/lib/rpm/macros.perl

Summary:	PostgreSQL table checker and dumper
Summary(pl):	Narzêdzie do sprawdzania baz systemu PostgreSQL
Name:		pgfsck
Version:	0.10
Release:	0.1
License:	BSD
Group:		Applications/Databases
Source0:	http://svana.org/kleptog/pgsql/%{name}-%{version}.tar.gz
URL:		http://svana.org/kleptog/pgsql/pgfsck.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostgreSQL table checker and dumper.

%description -l pl
Narzêdzie do sprawdzania baz systemu PostgreSQL.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{perl_sitelib}

install pgfsck $RPM_BUILD_ROOT%{_sbindir}
install *.pm $RPM_BUILD_ROOT%{perl_sitelib}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{perl_sitelib}/*
