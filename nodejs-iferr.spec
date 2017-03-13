%{?scl:%scl_package nodejs-iferr}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename iferr
%global enable_tests 0

Name:		%{?scl_prefix}nodejs-iferr
Version:	0.1.5
Release:	3%{?dist}
Summary:	Higher-order functions for easier error handling

License:	MIT
URL:		https://github.com/shesek/iferr
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	%{?scl_prefix}nodejs-devel
%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}coffee-script
BuildRequires:	%{?scl_prefix}mocha
%endif

%description
Higher-order functions for easier error handling

%prep
%setup -q -n package

# remove compiled script
#rm index.js

%build
# compile index.js from coffee-script
#%{_bindir}/coffee -c index.coffee

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%{_bindir}/mocha -R spec
%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Sep 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.5-3
- Built for RHSCL
- don't use coffee script

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 16 2015 Jared Smith <jsmith@fedoraproject.org> - 0.1.5-1
- Initial packaging
