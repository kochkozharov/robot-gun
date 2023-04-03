# Wifi setup

## Установка RaspberryPi OS

Инструкция предназначена для Linux (или любой другой POSIX-совместимой системы)

1. Скачать минимальное iso с https://www.raspberrypi.com/software/operating-systems/
2. Записать iso на флешку с помощью `sudo dd if=your-raspios-iso.img of=/dev/sdX bs=4M conv=fsync status=progress`
3. В `first_boot_setup/wpa_supplicant` указать SSID и пароль от вашей точки доступа WiFi.
4. Выполнить `echo "INSERT_YOUR_USER_PASSWORD_HERE" | openssl passwd -6 -stdin >> first_boot_setup/userconf.txt` 
5. В `/dev/sdX/bootfs` скопировать содержимое папки `first_boot_setup`
6. Вставить SD карту в RPi и подключить питание.
7. Подождать 1-2 минуты и выполнить `ssh admin@raspberrypi.local`. Если команда не работает, настроить Avahi на клиенте (или узнать локальный ip RPi с помощью `nmap -sP 192.168.1.0/24 ` и использоавть его вместо домена)
8. Ввести ранее заданный пароль.

## Настройка RaspberryPi os

Команды далее выполняются в SSH.

1. `sudo apt update`
2. `sudo apt full-upgrade`
3. `sudo apt install git vim`
4. `git clone https://gitlab.mai.ru/AlDGalkin/robot_gun/-/tree/main`
5. `cd robot_gun/wifi_setup`
6. `sudo ./setup.sh`
7. `sudo reboot`

После перезагрузки RPi автоматически начнет раздавать WiFi сеть под названием _robotgun_ c паролем _mai123456789,_ если не обнаружит сетей, указаных в `/etc/wpa_supplicant/wpa_supplicant.conf`, а так же запустит Flask-приложение на 5000-ом порту. IP RPi в сети _robotgun_ - `10.0.0.5`.