#!/usr/bin/env python
from importlib import import_module
import os
import RPi.GPIO as GPIO
import time
from markupsafe import escape
from flask import Flask, render_template, Response, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
pwm1 = GPIO.PWM(12, 100)
pwm2 = GPIO.PWM(13, 100)
pwm1.start(5)
pwm2.start(5)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/fire")
def fire():
    GPIO.setmode(GPIO.BCM)
    gpio_fire = 5
    gpio_signal=6
    GPIO.setup(gpio_signal, GPIO.IN)
    GPIO.setup(gpio_fire, GPIO.OUT)
    GPIO.output(gpio_fire, GPIO.HIGH)
    while GPIO.input(gpio_signal) == GPIO.HIGH:
        time.sleep(0.01)
    GPIO.setup(gpio_fire, GPIO.LOW)
    GPIO.cleanup(gpio_fire)
    return "ok"

@app.route('/servo1/<int:angle>')
def servo1(angle):
    duty = float(angle) / 2.5 + 2.5
    global pwm1
    pwm1.ChangeDutyCycle(duty)
    return "ok"

@app.route('/servo2/<int:angle>')
def servo2(angle):
    duty = float(angle) / 2.5 + 2.5
    global pwm2
    pwm2.ChangeDutyCycle(duty)
    return "ok"
