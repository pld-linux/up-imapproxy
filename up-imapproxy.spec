Summary:	Imapproxy Daemon
Summary(pl):	Serwer proxy dla protoko³u IMAP
Name:		up-imapproxy
Version:	1.2.3
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.imapproxy.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	ad4dafd1417903feb1e09ec569ff1ad5
Source1:	%{name}.init
URL:		http://www.imapproxy.org/
BuildRequires:	libwrap-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a connection caching imapproxy daemon for proxied imap
connections.

%description -l pl
Jest to buforuj±cy po³±czenia serwer proxy dla protoko³u IMAP,
po¶rednicz±cy w po³±czeniach IMAP.

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,%{_sbindir}}

install bin/* $RPM_BUILD_ROOT%{_sbindir}
install scripts/imapproxy.conf $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/imapproxy

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add imapproxy

%preun
/sbin/chkconfig --del imapproxy

%files
%defattr(644,root,root,755)
%doc README README.ssl ChangeLog
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/imapproxy.conf
%attr(754,root,root) /etc/rc.d/init.d/imapproxy
%attr(750,root,root) %{_sbindir}/*
