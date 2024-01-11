%global pypi_name pytest-subtests

Name:           python-%{pypi_name}
Version:        0.4.0
Release:        3%{?dist}
Summary:        Support for unittest subTest() and subtests fixture

License:        MIT
URL:            https://github.com/pytest-dev/pytest-subtests
Source0:        %{pypi_source}
BuildArch:      noarch

%description
pytest-subtests unittest subTest() support and subtests fixture.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description -n python3-%{pypi_name}
pytest-subtests unittest subTest() support and subtests fixture.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
# https://github.com/pytest-dev/pytest-subtests/issues/21
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=%{buildroot}%{python3_sitelib} \
  pytest-%{python3_version} -v tests \
  -k "not TestFixture and not TestCapture and not test_simple_terminal"

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_subtests.py
%{python3_sitelib}/pytest_subtests-%{version}-py*.egg-info/

%changelog
* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.4.0-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.4.0-2
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Sun Feb 07 2021 Christian Heimes <cheimes@redhat.com> - 0.4.0-1
- Update to 0.4 (#1925972)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-1
- Update to latest upstream release 0.3.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.9

* Mon Mar 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Initial package for Fedora
