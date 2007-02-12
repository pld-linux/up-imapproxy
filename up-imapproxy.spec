Summary:	Imapproxy Daemon
Summary(pl.UTF-8):	Serwer proxy dla protokołu IMAP
Name:		up-imapproxy
Version:	1.2.4
Release:	5
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.imapproxy.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	ad68dd2258255ac6ef87165f518390e9
Source1:	%{name}.init
Patch0:		%{name}-config.patch
Patch1:		%{name}-CVE-2005-2661.patch
URL:		http://www.imapproxy.org/
BuildRequires:	automake
BuildRequires:	libwrap-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	rc-scripts
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	libwrap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a connection caching imapproxy daemon for proxied imap
connections.

%description -l pl.UTF-8
Jest to buforujący połączenia serwer proxy dla protokołu IMAP,
pośredniczący w połączeniach IMAP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
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

%pre
%groupadd -g 150 imapproxy
%useradd -u 150 -c "IMAP proxy daemon" -g imapproxy imapproxy

%post
/sbin/chkconfig --add imapproxy
%service imapproxy restart "IMAP proxy daemon"

%preun
if [ "$1" = "0" ]; then
	%service imapproxy stop
	/sbin/chkconfig --del imapproxy
fi

%postun
if [ "$1" = "0" ]; then
	%userremove imapproxy
	%groupremove imapproxy
fi

%files
%defattr(644,root,root,755)
%doc README README.ssl ChangeLog
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/imapproxy.conf
%attr(754,root,root) /etc/rc.d/init.d/imapproxy
%attr(755,root,root) %{_sbindir}/*
