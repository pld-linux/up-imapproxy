Summary:	Imapproxy Daemon
Summary(pl):	Serwer proxy dla protokołu IMAP
Name:		up-imapproxy
Version:	1.2.1
Release:	0.2
License:        GPL
Group:		Networking/Daemons
Source0:	http://www.imapproxy.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	debd3edeb7441b9f713aaa9e9d7f2329
Source1:	up-imapproxy
URL:		http://www.imapproxy.org/
BuildRequires:	libwrap-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a connection caching imapproxy daemon for proxied imap
connections.

%description -l pl
Jest to buforujący połączenia serwer proxy dla protokołu IMAP,
pośredniczący w połączeniach IMAP.

%prep
%setup 

%build

%configure

%{__make} \
	CFLAGS="-I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_prefix}/sbin}

install bin/* $RPM_BUILD_ROOT%{_prefix}/sbin
install scripts/imapproxy.conf $RPM_BUILD_ROOT/etc
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/imapproxy

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add imapproxy

%preun
/sbin/chkconfig --del imapproxy 

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/imapproxy.conf
%attr(750,root,root) /etc/rc.d/init.d/imapproxy
%attr(750,root,root) %{_sbindir}/*
