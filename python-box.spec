# Created by pyp2rpm-3.3.2
%global pypi_name python-box
%global srcname box

Name:           python-%{srcname}
Version:        3.2.4
Release:        1%{?dist}
Summary:        Advanced Python dictionaries with dot notation access

License:        MIT
URL:            https://github.com/cdgriffith/Box
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(coverage) >= 3.6
BuildRequires:  python3dist(coverage) >= 3.6
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(setuptools)

%description
|BuildStatus| |CoverageStatus| |License| |PyPi| |DocStatus||BoxImage|Python
dictionaries with advanced dot notation access... code:: python from box import
Box movie_data { "movies": { "Spaceballs": { "imdb stars": 7.1, "rating": "PG",
"length": 96, "director": "Mel Brooks", "stars": [{"name": "Mel Brooks",
"imdb": "nm0000316", "role": "President Skroob"}, {"name": "John
Candy","imdb":...

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
 
Requires:       python3dist(coverage) >= 3.6
Requires:       python3dist(pytest)
Requires:       python3dist(pytest-cov)
%description -n python3-%{srcname}
|BuildStatus| |CoverageStatus| |License| |PyPi| |DocStatus||BoxImage|Python
dictionaries with advanced dot notation access... code:: python from box import
Box movie_data { "movies": { "Spaceballs": { "imdb stars": 7.1, "rating": "PG",
"length": 96, "director": "Mel Brooks", "stars": [{"name": "Mel Brooks",
"imdb": "nm0000316", "role": "President Skroob"}, {"name": "John
Candy","imdb":...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%doc README.rst
%{_bindir}/box.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/box.py
%{python3_sitelib}/python_box-%{version}-py?.?.egg-info

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 3.2.4-1
- Initial package.