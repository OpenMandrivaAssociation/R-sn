%global packname  sn
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.4.18
Release:          1
Summary:          The skew-normal and skew-t distributions
Group:            Sciences/Mathematics
License:          GPLv2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-18.tar.gz
BuildRequires:    R-devel R-mnormt R-sm
Requires:         R-core R-mnormt R-sm
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

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help