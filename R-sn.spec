%global packname  sn
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.4
Release:          18
Summary:          The skew-normal and skew-t distributions
Group:            Sciences/Mathematics
License:          GPLv2
URL:              http://cran.r-project.org/web/packages/sn/index.html
Source0:          http://cran.r-project.org/src/contrib/sn_0.4-18.tar.gz
Requires:         R-mnormt
BuildRequires:    R-devel
BuildArch:        noarch

%description
Functions for manipulating skew-normal and skew-t probability distributions,
and for fitting them to data, in the scalar and in the multivariate case.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}