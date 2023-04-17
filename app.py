#!/usr/bin/env python
from importlib import import_module
import os
import RPi.GPIO as GPIO
import time
from markupsafe import escape
from flask import Flask, render_template, Response, request
GPIO.setmode(GPIO.BCM)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/fire")
def fire():
    gpio_fire = 5
    gpio_signal=6
    GPIO.setup(gpio_signal, GPIO.IN)

    GPIO.setup(gpio_fire, GPIO.OUT)
    GPIO.output(gpio_fire, GPIO.HIGH)
    while GPIO.input(gpio_signal) == GPIO.HIGH:
        time.sleep(0.01)
    GPIO.cleanup()
    return "ok"


@app.route('/servo/<int:angle>')
def servo(angle):
    gpio_servo=13
    GPIO.setup(gpio_servo,GPIO.OUT)
    pwm = GPIO.PWM(gpio_servo,50)
    pwm.start(0)
    duty = angle / 18 + 2
    current_duty = pwm.get_duty_cycle()
    speed=10
    if current_duty < duty:
        for i in range(current_duty, duty, speed):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.02)
    else:
        for i in range(current_duty, duty, -speed):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.02)
    pwm.stop()
    GPIO.cleanup()
    return "ok"
