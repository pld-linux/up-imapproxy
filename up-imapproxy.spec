Summary:	Imapproxy Daemon
Summary(pl):	Serwer proxy dla protoko³u IMAP
Name:		up-imapproxy
Version:	1.2.1
Release:	0.1
License:        GPL
Group:		Networking/Daemons
Source0:	http://www.imapproxy.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	debd3edeb7441b9f713aaa9e9d7f2329
Patch0:		%{name}-curses.patch
URL:		http://www.imapproxy.org/
BuildRequires:	libwrap-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a connection caching imapproxy daemon for proxied imap
connections.

%description -l pl
Jest to buforuj±cy po³±czenia serwer proxy dla protoko³u IMAP,
po¶rednicz±cy w po³±czeniach IMAP.

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
