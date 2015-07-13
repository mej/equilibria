%{!?_rel:%{expand:%%global _rel 0.%(date '+%Y%m%d').%(git show -s --pretty=format:%h)}}

Summary: Simple Socket Proxy and Load Balancer
Name: equilibria
Version: 1.1
Release: %{_rel}%{?dist}
#Release: 1%{?dist}
License: BSD
Group: Applications/Internet
Source0: %{name}
Source1: %{name}.init
Source2: %{name}.conf
Source3: LICENSE
Source4: README.md
BuildArch: noarch
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Equilibria is a simple load-balancing socket proxy which can provide
basic packet forwarding, failover, and other useful Layer 3 features
between hosts, across firewalls, or among nodes in a cluster or grid.


%prep
cp %{SOURCE3} %{SOURCE4} .

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_sbindir} $RPM_BUILD_ROOT%{_initrddir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/log $RPM_BUILD_ROOT%{_localstatedir}/run/%{name}

%{__install} -m 0755 %{SOURCE0} $RPM_BUILD_ROOT%{_sbindir}/%{name}
%{__install} -m 0755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/%{name}
%{__install} -m 0600 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
touch $RPM_BUILD_ROOT%{_localstatedir}/log/%{name}.log


%post
/sbin/chkconfig --add %{name} >/dev/null 2>&1 || :


%postun
/sbin/service %{name} condrestart >/dev/null 2>&1 || :


%preun
if [ $1 -eq 0 ]; then
    /sbin/service %{name} stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del %{name} >/dev/null 2>&1 || :
fi


%files
%defattr(-, root, root, 0755)
%doc LICENSE README.md
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_sbindir}/%{name}
%{_initrddir}/%{name}
%{_localstatedir}/run/%{name}/
%ghost %{_localstatedir}/log/%{name}.log


%changelog
