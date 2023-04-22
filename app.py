#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import pigpio
from flask import Flask, render_template, Response
from camera_pi import Camera
from gpiozero.pins.pigpio import PiGPIOFactory
app = Flask(__name__)

servo2=12
pwm2=pigpio.pi()
pwm2.set_mode(servo2, pigpio.OUTPUT)
pwm2.set_PWM_frequency(servo2, 50)

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

#@app.route('/servo1/<int:anglea>')
#def servo1(angle):
#    global pwm1
#    pwm1.angle = angle
#    return "ok"

@app.route("/servo/<int:number>/<int:pulsewidth>")
def servo(number, pulsewidth):
    global pwm1, pwm2
    if pulsewidth>=500 and pulsewidth<=2500:
        if number==1:
            return "no"
        elif number==2:    
            pwm2.set_servo_pulsewidth(servo2,pulsewidth)
            return "ok"
        else:
            return "no"
    else:
        return "no"

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')

