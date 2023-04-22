#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, Response
from gpiozero import AngularServo
from camera_pi import Camera
app = Flask(__name__)

servo1 = AngularServo(12, initial_angle=60, min_angle=0, max_angle=120, min_pulse_width=1/1000, max_pulse_width=25/10000)
servo2 = AngularServo(13, initial_angle=60, min_angle=0, max_angle=120, min_pulse_width=1/1000, max_pulse_width=25/10000)

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
    global servo1
    servo1.angle
    return "ok"

@app.route('/servo2/<int:angle>')
def servo2(angle):
    global servo1
    servo1.angle
    return "ok"

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')

