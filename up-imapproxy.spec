Summary:	Imapproxy Daemon
Summary(proxy):	Serwer proxy dla imap'a
Name:		up-imapproxy
Version:	1.2.1
Release:	0.1
License:        GPL
Group:		Networking/Daemons
Source0:	http://www.imapproxy.org/downloads/%{name}-%{version}.tar.gz
Patch0:		%{name}-curses.patch
Url:		http://www.imapproxy.org
BuildRequires:	libwrap-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a connection caching imapproxy daemon for proxied imap connections.

%description -l pl
.

%prep
%setup 

%patch0 -p1

%build

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_prefix}/sbin}

install bin/* $RPM_BUILD_ROOT%{_prefix}/sbin
install scripts/imapproxy.conf $RPM_BUILD_ROOT/etc
install scripts/imapproxy.init $RPM_BUILD_ROOT/etc/rc.d/init.d/imapproxy

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -f /etc/imapproxy.conf ]; then
	cp -a /etc/imapproxy.conf /etc/imapproxy.conf.old
fi


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
