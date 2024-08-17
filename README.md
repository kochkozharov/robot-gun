# Robot_gun

### **Тема проекта**
Проектирование метательного устройства

### **Цель проекта**
Сделать управляемую пушку на робособаку, которая будет демонстрироваться на дне открытых дверей.

### **Задача проекта**
1. Проработка концепции  
2. Изучение необходимой литературы 
3. Установка пушки
4. Создание контроллера
5. Исправление багов серводвигателей и пушки


### **Команда**

|ФИО| Роль | Задача |
|---|---|---|
|Галкин Алексей Дмитриевич| Тимлид| Координация действий участников, распределение задач команды|
|Цирулев Николай Владимирович| Fullstack-разработчик| Создание контроллера| 
|Слетюрин Кирилл Сергеевич|Физик-электрик| Создание электрической схемы |
|Кудрявов Леонид Вадимович| 3D моделист| Создание 3D модели|
|Кочкожаров Иван Вячеславович| DevOps| Настройка операционной системы |

### **Заказчик проекта**
Кафедра 806 “Вычислительная математика и программирование”.

### **Конечный пользователь**
Абитуриенты МАИ, кафедра 806, посетители дней открытых дверей.

### **Ссылки**
Miro: https://miro.com/app/board/uXjVPhjRGJ0=/     
Trello: https://trello.com/b/Ce0M3ckV/проект      
Паспорт проекта: https://docs.google.com/document/d/1gG5YquecGiLvQ7yznsQgO7weUjUDbJEx/edit

Дата начала проекта: 20.02.2023

Дата окончания проекта: 30.04.2023

# Схема

![alt text](https://github.com/kochkozharov/robot-gun/blob/main/Robogun_-_%D0%A4%D0%B8%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%81%D1%85%D0%B5%D0%BC%D0%B0.jpg)


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