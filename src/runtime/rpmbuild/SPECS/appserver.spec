%define         _unpackaged_files_terminate_build 0
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Name:       ${build.name.prefix}runtime
Version:    ${appserver.runtime.semver}
Release:    ${appserver.runtime.suffix}${build.name.suffix}
Summary:    appserver.io provides a multithreaded application server for PHP.
Group:      System Environment/Base
License:    OSL 3.0
Vendor:     Bernhard Wick bw@appserver.io
URL:        http://appserver.io
requires:   git, libmcrypt
Provides:   appserver-runtime

%description
%{summary}

%prep

%build

%clean

%files
/opt/appserver/bin/*
/opt/appserver/etc/*
/opt/appserver/include/*
/opt/appserver/lib/*
/opt/appserver/php/*
/opt/appserver/sbin/*
/opt/appserver/var/*

%post
# Reload shared library list
ldconfig

# Create composer symlink
ln -sf /opt/appserver/bin/composer.phar /opt/appserver/bin/composer

# do the calling home for statistics
user_id = uuidgen
curl -X POST --user-agent "${analytics.user.agent}" --data "v=1&tid=${analytics.runtime.property-id}&an=appserver-runtime&t=screenview&cid=$user_id&av=${appserver.src.version}&aid=${analytics.app.id}&aiid=${analytics.app.installer}&cd=installation" ${analytics.base.url}

%postun
# Reload shared library list
ldconfig