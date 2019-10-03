%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-vcsrepo
%global commit b06d5d378e80d03c5dea40a89e83449191064ddc
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-vcsrepo
Version:        3.0.0
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
* Thu Oct 3 2019 RDO <dev@lists.rdoproject.org> 3.0.0-1.b06d5d3git
- Update to post 3.0.0 (b06d5d378e80d03c5dea40a89e83449191064ddc)



