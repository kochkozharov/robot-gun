#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response, request, session
from camera_pi import Camera
from move_servo import Servo

myServo = Servo()
app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html', data=[str(myServo.x), str(myServo.y), myServo.p])

@app.route('/login', methods=['POST'])
def admin_login():
    if request.form['password'] == '777' and request.form['login'] == 'admin':
        session['logged_in'] = True
    else:
        session['logged_in'] = False
    return index()

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(gen(Camera()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/test", methods=["POST"])
def test():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        myServo.moveto(int(request.form["slider1"]),int(request.form["slider2"]),
                       [int(request.form["p1"]),int(request.form["p3"]),int(request.form["p2"]),
                        int(request.form["p4"]),int(request.form["p5"]),int(request.form["p6"]),
                        int(request.form["p7"]),int(request.form["p8"]),int(request.form["p9"]),
                        int(request.form["p10"]),int(request.form["p11"]),int(request.form["p12"]),
                        int(request.form["p13"])])
        return render_template('index.html', data=[str(myServo.x), str(myServo.y), myServo.p])

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host='192.168.1.34', threaded=True)