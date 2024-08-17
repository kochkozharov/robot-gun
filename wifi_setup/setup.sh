#!/usr/bin/env bash
apt install hostapd dnsmasq pigpio python3-venv -y &&
systemctl unmask hostapd &&
systemctl disable hostapd &&
systemctl disable dnsmasq &&
cp /home/admin/robot_gun/wifi_setup/files/hostapd.conf /etc/hostapd/ &&
cp /home/admin/robot_gun/wifi_setup/files/hostapd /etc/default/ &&
mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig &&
cp /home/admin/robot_gun/wifi_setup/files/dnsmasq.conf /etc/ &&
cp /home/admin/robot_gun/wifi_setup/files/autohotspot /usr/bin/ &&
cp /home/admin/robot_gun/wifi_setup/files/interfaces /etc/network/ &&
cp /home/admin/robot_gun/wifi_setup/files/autohotspot.service /etc/systemd/system/ &&
cp /home/admin/robot_gun/wifi_setup/files/robotgun.service /etc/systemd/system/ &&
cp /home/admin/robot_gun/wifi_setup/files/dhcpcd.conf /etc &&
python3 -m venv /home/admin/robot_gun/venv &&
. /home/admin/robot_gun/venv/bin/activate && 
pip install -r /home/admin/robot_gun/requirements.txt &&
systemctl enable autohotspot.service &&
systemctl enable robotgun.service &&
systemctl enable pigpiod.service
