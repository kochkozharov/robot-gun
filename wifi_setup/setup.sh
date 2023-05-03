#!/usr/bin/env bash
sudo apt install hostapd dnsmasq pigpio -y
sudo systemctl unmask hostapd
sudo systemctl disable hostapd
sudo systemctl disable dnsmasq
sudo cp /home/admin/robot_gun/wifi_setup/files/hostapd.conf /etc/hostapd/
sudo cp /home/admin/robot_gun/wifi_setup/files/hostapd /etc/default/
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
sudo cp /home/admin/robot_gun/wifi_setup/files/dnsmasq.conf /etc/
sudo cp /home/admin/robot_gun/wifi_setup/files/autohotspot /usr/bin/
sudo cp /home/admin/robot_gun/wifi_setup/files/interfaces /etc/network/
sudo cp /home/admin/robot_gun/wifi_setup/files/autohotspot.service /etc/systemd/system/
sudo cp /home/admin/robot_gun/wifi_setup/files/robotgun.service /etc/systemd/system/
sudo echo "nohook wpa_supplicant" >> /etc/dhcpcd.conf
sudo python3 -m venv /home/admin/robot_gun/venv
sudo . /home/admin/robot_gun/venv/bin/activate
sudo pip install -r /home/admin/robot_gun/requirements.txt
sudo systemctl enable autohotspot.service
sudo systemctl enable robotgun.service
sudo systemctl enable pigpio.service