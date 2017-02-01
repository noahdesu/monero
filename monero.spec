Name:		monero
Version:	1
Release:	1%{?dist}
Summary:	Monero is a private, secure, untraceable, decentralised digital currency.
License:	BSD
#Source0:	https://github.com/monero-project/monero/archive/v0.10.1.tar.gz
Source0:    monero-1.tar.gz
BuildRequires: cmake
BuildRequires: openssl-devel
BuildRequires: boost-devel

%description
Monero is a private, secure, untraceable, decentralised digital currency. You
are your bank, you control your funds, and nobody can trace your transfers
unless you allow them to do so.

%prep
%autosetup

%build
make %{?_smp_mflags}

%install

mkdir -p %{buildroot}/%{_bindir}
pushd build/release/bin
install -p -m 755 monero-blockchain-export %{buildroot}%{_bindir}
install -p -m 755 monero-blockchain-import %{buildroot}%{_bindir}
install -p -m 755 monerod %{buildroot}%{_bindir}
install -p -m 755 monero-utils-deserialize %{buildroot}%{_bindir}
install -p -m 755 monero-wallet-cli %{buildroot}%{_bindir}
install -p -m 755 monero-wallet-rpc %{buildroot}%{_bindir}
popd

%files

%{_bindir}/monero-blockchain-export
%{_bindir}/monero-blockchain-import
%{_bindir}/monerod
%{_bindir}/monero-utils-deserialize
%{_bindir}/monero-wallet-cli
%{_bindir}/monero-wallet-rpc

%license LICENSE
