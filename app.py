#!/usr/bin/env python
from importlib import import_module
import os
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, Response, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/fire")
def fire():
    GPIO.setmode(GPIO.BCM)
    gpio_value = 5
    GPIO.setup(gpio_value, GPIO.OUT)
    GPIO.output(gpio_value, GPIO.HIGH)
    time.sleep(1)
    GPIO.cleanup()
    return "ok"