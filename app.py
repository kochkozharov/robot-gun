#!/usr/bin/env python
from importlib import import_module
import os
import RPi.GPIO as GPIO
import time
from markupsafe import escape
from flask import Flask, render_template, Response, request
app = Flask(__name__)

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
    GPIO.cleanup()
    return "ok"


@app.route('/servo/<int:angle>')
def servo(angle):
    GPIO.setmode(GPIO.BCM)
    gpio_servo=13
    GPIO.setup(gpio_servo, GPIO.OUT)
    pwm = GPIO.PWM(gpio_servo,50)
    pwm.start(angle_to_percent(0))
    time.sleep(1)
    pwm.ChangeDutyCycle(angle_to_percent(angle))
    time.sleep(1)
    pwm.stop()
    GPIO.cleanup()
    return "ok"

def angle_to_percent (angle) :
    minDC = 1.75
    maxDC = 13.15
    requiredDC = (angle/180*(maxDC-minDC)+minDC)/100*2000
    return requiredDC
