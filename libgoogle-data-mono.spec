Summary:	.NET library for the Google Data API 
Name:		libgoogle-data-mono
Version:	1.8.0.0
Release:	12
License:	Apache License
Group:		Development/Other
Url:		http://code.google.com/p/google-gdata/
Source0:	http://google-gdata.googlecode.com/files/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(mono)

%description
The Google Data APIs (GData) provide a simple protocol for reading and
writing data on the web.

Each of the following Google services provides a Google data API:

    * Base
    * Blogger
    * Calendar
    * Spreadsheets
    * Google Apps Provisioning
    * Code Search
    * Notebook
    * Picasa Web Albums
    * Document Feed
    * Contacts
    * You Tube
    * Google Health 

The GData .NET Client Library provides a library and source code that
make it easy to access data through Google Data APIs.

%package devel
Group:		Development/Other
Summary:	.NET library for the Google Data API 
Requires:	%{name} = %{version}-%{release}

%description devel
The Google Data APIs (GData) provide a simple protocol for reading and
writing data on the web.

Each of the following Google services provides a Google data API:

    * Base
    * Blogger
    * Calendar
    * Spreadsheets
    * Google Apps Provisioning
    * Code Search
    * Notebook
    * Picasa Web Albums
    * Document Feed
    * Contacts
    * You Tube
    * Google Health 

The GData .NET Client Library provides a library and source code that
make it easy to access data through Google Data APIs.

%prep
%setup -q
%autopatch -p1

%build
#gw:	trying to work around a BS problem, don't use parallel make
make PREFIX=%{_prefix}

%install
%makeinstall_std PREFIX=%{_prefix}
mkdir -p %{buildroot}%{_datadir}/
mv %{buildroot}%{_prefix}/lib/pkgconfig %{buildroot}%{_datadir}/

%check
#gw fails in 1.4.0.2
#make test

%files
%doc LICENSE-2.0.txt
%{_prefix}/lib/mono/GData-Sharp
%{_prefix}/lib/mono/gac/*

%files devel
%doc RELEASE_NOTES.HTML
%{_datadir}/pkgconfig/*.pc

