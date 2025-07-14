%define		_name	libpcap
%define		_ver	0.9.3
Summary:	Libpcap provides promiscuous mode access to network interfaces
Summary(es.UTF-8):	libpcap ofrece acceso a modo promiscuo en interfaces de red
Summary(pl.UTF-8):	Libpcap pozwala na bezpośredni dostęp do interfejsów sieciowych
Summary(pt_BR.UTF-8):	A libpcap fornece acesso ao modo promíscuo em interfaces de rede
Summary(ru.UTF-8):	Предоставляет доступ к сетевым интерфейсам в promiscuous-режиме
Summary(uk.UTF-8):	Надає доступ до мережевих інтерфейсів в promiscuous-режимі
Name:		libpcap_mmap
Version:	0.9.20060417
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://public.lanl.gov/cpw/%{_name}-%{version}.tar.gz
# Source0-md5:	21a2c20583d69a0153863145a7382aec
Patch0:		%{name}-soname.patch
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool
Provides:	libpcap = 2:0.9.4-1
Obsoletes:	libpcap
Obsoletes:	libpcap0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libpcap is a system-independent interface for user-level packet
capture. Libpcap provides a portable framework for low-level network
monitoring. Applications include network statistics collection,
security monitoring, network debugging, etc. Libpcap has
system-independent API that is used by several applications, including
tcpdump and arpwatch.

This libpcap version which supports MMAP mode on the Linux kernel
2.[46].x.

%description -l es.UTF-8
libpcap es una interface independiente de sistema para captura de
paquetes en modo usuario. Ofrece un esquema portátil para el control
de la red en bajo nivel. Se utiliza para colecta de estadísticas de
red, Control de seguridad, depuración de la red, etc. Tiene una API
independiente de sistema que se usa por varias aplicaciones, entre
ellas tcpdump y arpwatch.

%description -l pl.UTF-8
libpcap to niezależny od systemu interfejs do przechwytywania pakietów
z poziomu użytkownika.

Wersja ta obsługuje tryb MMAP obsługiwany przez jądra 2.4.x i 2.6.x.

%description -l pt_BR.UTF-8
A libpcap é uma interface independente de sistema para captura de
pacotes em modo usuário. Fornece um esquema portátil para monitoração
da rede em baixo nível. É utilizada para coleta de estatísticas de
rede, monitoramento de segurança, depuração da rede, etc. Tem uma API
independente de sistema que é usada por várias aplicações, entre elas
tcpdump e arpwatch.

%description -l ru.UTF-8
Libpcap - это системнонезависимый интерфейс для захвата пакетов с
пользовательского уровня и низкоуровневого сетевого мониторинга.
Возможные применения включают сбор сетевой статистики, наблюдение за
безопасностью, отладка сети и т.д. Libpcap имеет системнонезависимый
API, используемый многими приложениями, включая tcpdump и arpwatch.

%description -l uk.UTF-8
Libpcap - це системнонезалежний інтерфейс для захвату пакетів з рівня
користувача та нізкорівневого моніторингу мережі. Можливі використання
включають збір статистики мережі, спостереження за безпекою, відладка
мережі і т.і. Libpcap має системнонезалежний API що використовується
багатьма програмами, такими ял tcpdump, arpwatch та trafshow.

%package devel
Summary:	Header files and develpment documentation for libpcap
Summary(es.UTF-8):	Arquivos de cabeçalho e bibliotecas de desenvolvimento para libpcap
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumetacja do libpcap
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para a libpcap
Summary(ru.UTF-8):	Хедеры и библиотеки програмиста для libpcap
Summary(uk.UTF-8):	Хедери та бібліотеки програміста для libpcap
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	libpcap-devel = 2:0.9.4-1
Obsoletes:	libpcap-devel
Obsoletes:	libpcap0-devel

%description devel
Libpcap provides a portable framework for low-level network
monitoring. Libpcap can provide network statistics collection,
security monitoring and network debugging. Since almost every system
vendor provides a different interface for packet capture, the libpcap
authors created this system-independent API to ease in porting and to
alleviate the need for several system-dependent packet capture modules
in each application.

Install libpcap if you need to do low-level network traffic monitoring
on your network.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libpcap.

%description devel -l pt_BR.UTF-8
Tcpdump imprime os cabeçalhos dos pacotes em uma interface de rede.
Ele é muito prático para resolver problemas na rede e para operações
de segurança.

%description devel -l ru.UTF-8
Хедеры и библиотеки програмиста, необходимые для программирования с
libpcap.

%description devel -l uk.UTF-8
Хедери та бібліотеки програміста, необхідні для програмування з
libpcap.

%package static
Summary:	Static libpcap library
Summary(es.UTF-8):	Biblioteca estática usada no desenvolvimento de aplicativos com libpcap
Summary(pl.UTF-8):	Biblioteka statyczna libpcap
Summary(pt_BR.UTF-8):	Biblioteca estática de desenvolvimento
Summary(ru.UTF-8):	Статическая библиотека libpcap
Summary(uk.UTF-8):	Статична бібліотека libpcap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libpcap-static = 2:0.9.4-1
Obsoletes:	libpcap-static

%description static
Libpcap provides a portable framework for low-level network
monitoring. Libpcap can provide network statistics collection,
security monitoring and network debugging. Since almost every system
vendor provides a different interface for packet capture, the libpcap
authors created this system-independent API to ease in porting and to
alleviate the need for several system-dependent packet capture modules
in each application.

This package contains the static library used for development.

%description static -l pt_BR.UTF-8
Tcpdump imprime os cabeçalhos dos pacotes em uma interface de rede.
Ele é muito prático para resolver problemas na rede e para operações
de segurança.

%description static -l pl.UTF-8
Biblioteka statyczna libpcap.

%description static -l ru.UTF-8
Статическая библиотека, необходимая для программирования с libpcap.

%description static -l uk.UTF-8
Статична бібліотека, необхідна для програмування з libpcap.

%prep
%setup -q -n %{_name}-%{version}
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_includedir}/net
install -d $RPM_BUILD_ROOT%{_mandir}/man3

install pcap.3 		$RPM_BUILD_ROOT%{_mandir}/man3

install pcap.h 		$RPM_BUILD_ROOT%{_includedir}
install pcap-bpf.h 	$RPM_BUILD_ROOT%{_includedir}/net
install pcap-int.h	$RPM_BUILD_ROOT%{_includedir}
install pcap-namedb.h	$RPM_BUILD_ROOT%{_includedir}
install pcap-septel.h	$RPM_BUILD_ROOT%{_includedir}
install pcap-dag.h	$RPM_BUILD_ROOT%{_includedir}
install pcap-ring.h	$RPM_BUILD_ROOT%{_includedir}

./libtool --mode=install install libpcap.la $RPM_BUILD_ROOT%{_libdir}

# some packages want it... but sanitize somehow
# (don't depend on HAVE_{STRLCPY,SNPRINTF,VSNPRINTF} defines)
sed -e '279,285d;288,297d' pcap-int.h > $RPM_BUILD_ROOT%{_includedir}/pcap-int.h

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS LICENSE README README.ring README.linux README.dag README.septel VERSION REVISION doc/pcap.*
%attr(755,root,root) %{_libdir}/libpcap.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpcap.so
%{_includedir}/*.h
%{_includedir}/net/*.h
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpcap.a
