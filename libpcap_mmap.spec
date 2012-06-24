%define		_name	libpcap
%define		_ver	0.9.3
Summary:	Libpcap provides promiscuous mode access to network interfaces
Summary(es):	libpcap ofrece acceso a modo promiscuo en interfaces de red
Summary(pl):	Libpcap pozwala na bezpo�redni dost�p do interfejs�w sieciowych
Summary(pt_BR):	A libpcap fornece acesso ao modo prom�scuo em interfaces de rede
Summary(ru):	������������� ������ � ������� ����������� � promiscuous-������
Summary(uk):	����� ������ �� ��������� ��������Ӧ� � promiscuous-����ͦ
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

%description -l es
libpcap es una interface independiente de sistema para captura de
paquetes en modo usuario. Ofrece un esquema port�til para el control
de la red en bajo nivel. Se utiliza para colecta de estad�sticas de
red, Control de seguridad, depuraci�n de la red, etc. Tiene una API
independiente de sistema que se usa por varias aplicaciones, entre
ellas tcpdump y arpwatch.

%description -l pl
libpcap to niezale�ny od systemu interfejs do przechwytywania pakiet�w
z poziomu u�ytkownika.

Wersja ta obs�uguje tryb MMAP obs�ugiwany przez j�dra 2.4.x i 2.6.x.

%description -l pt_BR
A libpcap � uma interface independente de sistema para captura de
pacotes em modo usu�rio. Fornece um esquema port�til para monitora��o
da rede em baixo n�vel. � utilizada para coleta de estat�sticas de
rede, monitoramento de seguran�a, depura��o da rede, etc. Tem uma API
independente de sistema que � usada por v�rias aplica��es, entre elas
tcpdump e arpwatch.

%description -l ru
Libpcap - ��� ������������������� ��������� ��� ������� ������� �
����������������� ������ � ��������������� �������� �����������.
��������� ���������� �������� ���� ������� ����������, ���������� ��
�������������, ������� ���� � �.�. Libpcap ����� �������������������
API, ������������ ������� ������������, ������� tcpdump � arpwatch.

%description -l uk
Libpcap - �� ������������������ ��������� ��� ������� ����Ԧ� � Ҧ���
����������� �� Φ���Ҧ������� ��Φ������� ����֦. �����צ ������������
��������� �¦� ���������� ����֦, ������������� �� ��������, צ������
����֦ � �.�. Libpcap ��� ������������������ API �� ����������դ����
�������� ����������, ������ �� tcpdump, arpwatch �� trafshow.

%package devel
Summary:	Header files and develpment documentation for libpcap
Summary(es):	Arquivos de cabe�alho e bibliotecas de desenvolvimento para libpcap
Summary(pl):	Pliki nag��wkowe i dokumetacja do libpcap
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para a libpcap
Summary(ru):	������ � ���������� ����������� ��� libpcap
Summary(uk):	������ �� ¦�̦����� ������ͦ��� ��� libpcap
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

%description devel -l pl
Pliki nag��wkowe i dokumentacja do libpcap.

%description devel -l pt_BR
Tcpdump imprime os cabe�alhos dos pacotes em uma interface de rede.
Ele � muito pr�tico para resolver problemas na rede e para opera��es
de seguran�a.

%description devel -l ru
������ � ���������� �����������, ����������� ��� ���������������� �
libpcap.

%description devel -l uk
������ �� ¦�̦����� ������ͦ���, ����Ȧ�Φ ��� ������������� �
libpcap.

%package static
Summary:	Static libpcap library
Summary(es):	Biblioteca est�tica usada no desenvolvimento de aplicativos com libpcap
Summary(pl):	Biblioteka statyczna libpcap
Summary(pt_BR):	Biblioteca est�tica de desenvolvimento
Summary(ru):	����������� ���������� libpcap
Summary(uk):	�������� ¦�̦����� libpcap
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

%description static -l pt_BR
Tcpdump imprime os cabe�alhos dos pacotes em uma interface de rede.
Ele � muito pr�tico para resolver problemas na rede e para opera��es
de seguran�a.

%description static -l pl
Biblioteka statyczna libpcap.

%description static -l ru
����������� ����������, ����������� ��� ���������������� � libpcap.

%description static -l uk
�������� ¦�̦�����, ����Ȧ��� ��� ������������� � libpcap.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

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
