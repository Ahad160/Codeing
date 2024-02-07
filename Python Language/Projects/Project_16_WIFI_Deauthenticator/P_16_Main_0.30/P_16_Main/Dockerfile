FROM 3.12.0rc1

ENV DEBIAN_FRONTEND noninteractive
ENV HASHCAT_VERSION hashcat-6.2.6
ENV HASHCAT_UTILS_VERSION 1.9

# Install requirements
FROM debian:trixie
RUN apt update && apt upgrade -y
RUN apt install clang ca-certificates gcc openssl make kmod nano wget p7zip build-essential libsqlite3-dev libpcap0.8-dev libpcap-dev sqlite3 pkg-config libnl-genl-3-dev libssl-dev net-tools iw ethtool usbutils pciutils wireless-tools git curl wget unzip macchanger tshark -y
RUN apt build-dep aircrack-ng -y

# Install Aircrack from Source
RUN wget https://download.aircrack-ng.org/aircrack-ng-1.7.tar.gz
RUN tar xzvf aircrack-ng-1.7.tar.gz
WORKDIR /aircrack-ng-1.7/
RUN autoreconf -i
RUN ./configure --with-experimental
RUN make
RUN make install
RUN airodump-ng-oui-update

# Workdir /
WORKDIR /

