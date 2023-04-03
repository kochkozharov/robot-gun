#!/usr/bin/env bash
apt install hostapd dnsmasq -y
systemctl unmask hostapd
systemctl disable hostapd
systemctl disable dnsmasq
cp files/hostapd.conf /etc/hostapd/
cp files/hostapd /etc/default/
mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
cp files/dnsmasq.conf /etc/
cp files/autohotspot /usr/bin/
cp files/interfaces /etc/network/
cp files/autohotspot.service files/robotgun.service /etc/systemd/system/
echo "nohook wpa_supplicant" >> /etc/dhcpcd.conf
systemctl enable autohotspot.service
systemctl enable robotgun.serviceh