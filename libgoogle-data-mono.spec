Summary: .NET library for the Google Data API 
Name:    libgoogle-data-mono
Version: 1.8.0.0
Release: 3
Source0: http://google-gdata.googlecode.com/files/%{name}-%{version}.tar.gz
License: Apache License
Group: Development/Other
Url: http://code.google.com/p/google-gdata/
BuildRequires: mono-devel
BuildArch: noarch

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
Group: Development/Other
Summary:.NET library for the Google Data API 
Requires: %name = %version-%release

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
%apply_patches

%build
#gw: trying to work around a BS problem, don't use parallel make
make PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix
mkdir -p %buildroot%_datadir/
mv %buildroot%_prefix/lib/pkgconfig %buildroot%_datadir/

%check
#gw fails in 1.4.0.2
#make test

%files
%doc LICENSE-2.0.txt
%_prefix/lib/mono/GData-Sharp
%_prefix/lib/mono/gac/*

%files devel
%doc RELEASE_NOTES.HTML
%_datadir/pkgconfig/*.pc




%changelog
* Fri May 20 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.8.0.0-2
+ Revision: 676311
- Clean spec file for rpm5

* Fri May 20 2011 Funda Wang <fwang@mandriva.org> 1.8.0.0-1
+ Revision: 676282
- new version 1.8.0.0

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.0.0-2
+ Revision: 660258
- mass rebuild

* Mon Aug 23 2010 Götz Waschk <waschk@mandriva.org> 1.6.0.0-1mdv2011.0
+ Revision: 572482
- new version
- drop patch
- update file list

* Thu Mar 11 2010 Götz Waschk <waschk@mandriva.org> 1.4.0.2-3mdv2010.1
+ Revision: 518276
- fix pkgconfig file again

* Thu Mar 11 2010 Götz Waschk <waschk@mandriva.org> 1.4.0.2-2mdv2010.1
+ Revision: 518267
- fix path in pkgconfig files

* Thu Mar 11 2010 Götz Waschk <waschk@mandriva.org> 1.4.0.2-1mdv2010.1
+ Revision: 518252
- import libgoogle-data-mono


