#!/usr/bin/env python
from time import sleep, strftime, time
from gpiozero import CPUTemperature
cpu = CPUTemperature()
with open("/home/admin/cpu_temp.csv", "a") as log:
    while True:
        temp = cpu.temperature
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
        print("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
        sleep(10)
