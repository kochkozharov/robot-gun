#!/usr/bin/env python
from importlib import import_module
import os
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, Response, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        button_value = request.form['button_value']
        if button_value == 'value':
            GPIO.setmode(GPIO.BOARD)
            gpio_value = 15
            GPIO.setup(gpio_value, GPIO.OUT)
            GPIO.output(gpio_value, GPIO.HIGH)
            time.sleep(1)
            GPIO.cleanup()
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
