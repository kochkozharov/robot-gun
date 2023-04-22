#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, Response
from gpiozero import AngularServo
from camera_pi import Camera
from gpiozero.pins.pigpio import PiGPIOFactory
app = Flask(__name__)
factory = PiGPIOFactory()
pwm1 = AngularServo(12, initial_angle=0, min_angle=0, max_angle=120, min_pulse_width=1/1000, max_pulse_width=25/10000, pin_factory=factory)
pwm2 = AngularServo(13, initial_angle=0, min_angle=0, max_angle=120, min_pulse_width=1/1000, max_pulse_width=25/10000, pin_factory=factory)

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
    global pwm1
    pwm1.angle = angle
    return "ok"

@app.route('/servo2/<int:angle>')
def servo2(angle):
    global pwm2
    pwm2.angle = angle
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

