%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-vcsrepo
%global commit e5d9e4c8ce059e369f5c5bbd4b49f1fc908feae1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-vcsrepo
Version:        6.1.0
Release:        1%{?alphatag}%{?dist}
Summary:        Puppet module providing a type to manage repositories from various version control systems
License:        GPLv2

URL:            https://github.com/puppetlabs/puppetlabs-vcsrepo

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
Puppet module providing a type to manage repositories from various version control systems

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/vcsrepo/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/vcsrepo/



%files
%{_datadir}/openstack-puppet/modules/vcsrepo/


%changelog
* Wed Oct 11 2023 RDO <dev@lists.rdoproject.org> 6.1.0-1.e5d9e4cgit
- Update to post 6.1.0 (e5d9e4c8ce059e369f5c5bbd4b49f1fc908feae1)



