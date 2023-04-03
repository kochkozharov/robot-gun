#!/usr/bin/env bash
apt install hostapd dnsmasq -y
systemctl unmask hostapd
systemctl disable hostapd
systemctl disable dnsmasq

cp files/autohotspot /usr/bin
cp files/autohotspot.service files/robotgun.service /etc/systemd/system

#TODO Дописать скрипт