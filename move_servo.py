from adafruit_servokit import ServoKit
import time

class Servo(object):
    """ Class to move servos """
        
    def __init__(self):
        """Constructor"""
        self.x = 90
        self.y = 90
        self.p = [90,90,90, 90,90,90, 90,90,90, 90,90,90, 1]
        
        self.kit = ServoKit(channels=16)
        self.kit.servo[1].set_pulse_width_range(480, 2400)
        self.kit.servo[2].set_pulse_width_range(480, 2400)
        self.kit.servo[3].set_pulse_width_range(600, 2500)
        self.kit.servo[4].set_pulse_width_range(480, 2450)
        self.kit.servo[5].set_pulse_width_range(430, 2340)
        self.kit.servo[6].set_pulse_width_range(560, 2500)
        self.kit.servo[7].set_pulse_width_range(570, 2520)
        self.kit.servo[8].set_pulse_width_range(630, 2550)
        self.kit.servo[9].set_pulse_width_range(530, 2420)
        self.kit.servo[10].set_pulse_width_range(470, 2470)
        self.kit.servo[11].set_pulse_width_range(470, 2400)
        self.kit.servo[12].set_pulse_width_range(500, 2420)
        self.kit.servo[14].set_pulse_width_range(480, 2400)
        self.kit.servo[15].set_pulse_width_range(480, 2400)
    
    def moveto(self, nx, ny, pp):
        """
        Move camera to position
        """       
        if 0 <= nx <= 180:
            self.x = nx
            self.kit.servo[15].angle = 180 - nx      
        
        if 0 <= ny <= 180:
            self.y = ny
            self.kit.servo[14].angle = ny

        for i in range(0,12):
            if pp[12] == 0:
                self.p[12] = 0
                self.kit.servo[i+1].angle = None
            else:
                self.p[12] = 1
                if 0 <= pp[i] <= 180:
                    self.p[i] = pp[i]
                    self.kit.servo[i+1].angle = pp[i]

        return True
