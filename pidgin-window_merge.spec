Name:          pidgin-window_merge
Version:       0.3
Release:       1%{?dist}
Summary:       Merges the Buddy List window with a conversation window

Group:         Applications/Internet
License:       GPLv3+
URL:           https://github.com/dm0-/window_merge
Source0:       https://github.com/downloads/dm0-/window_merge/window_merge-0.3.tar.gz

BuildRequires: pidgin-devel
Requires:      pidgin

%global pname     %(echo -n %{name} | sed s/^pidgin-//)
%global plugindir %(pkg-config --variable=plugindir pidgin)

%description
Enabling this plugin will allow conversations to be attached to the Buddy List
window.  Preferences are available to customize the plugin's panel layout.


%prep
%setup -qn %{pname}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} plugindir=%{plugindir}
rm -f %{buildroot}%{plugindir}/%{pname}.la


%files
%{plugindir}/%{pname}.so
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO


%changelog
* Tue Jul 10 2012 David Michael <fedora.dm0@gmail.com> - 0.3-1
- Update to a newer release

* Mon Mar 26 2012 David Michael <fedora.dm0@gmail.com> - 0.2-1
- Update to a newer release

* Fri Mar 16 2012 David Michael <fedora.dm0@gmail.com> - 0.1-1
- Initial package
