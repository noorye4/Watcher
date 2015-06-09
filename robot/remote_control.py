#!/usr/bin/env python
# -*- coding:utf8 -*-
from ev3.lego import LargeMotor
from time import sleep

motor_A = LargeMotor(port='A')
motor_B = LargeMotor(port='B')
motor_A.stop_mode='hold'
motor_B.stop_mode='hold'

# motor_A.stop_mode='hold'
# motor_B.stop_mode='hold'
# motor_C.stop_mode='hold'
motor_speed = 900
compass_speed = 300


def forward():
    motor_A.run_forever(motor_speed,speed_regulation=True)
    motor_B.run_forever(motor_speed,speed_regulation=True)

def back():
    motor_A.run_forever(-motor_speed,speed_regulation=True)
    motor_B.run_forever(-motor_speed,speed_regulation=True)

def turn_left():
    motor_A.run_forever(-300,speed_regulation=True)
    motor_B.run_forever(300,speed_regulation=True)

def turn_right():
    motor_A.run_forever(300,speed_regulation=True)
    motor_B.run_forever(-300,speed_regulation=True)

def stop():
    motor_A.run_forever(0,speed_regulation=True)
    motor_B.run_forever(0,speed_regulation=True)


print "input a control key"
while True:
    key = raw_input()
    if key == 'w':
        print "forward"
        forward()
    if key == 'a':
        print "turn left"
        turn_left()
    if key == 's':
        print "back"
        back()
    if key == 'd':
        print "turn right"
        turn_right()
    if key == 'e':
        print "stop"
        stop()
    if key == 'q':
        print "quit"
        break
    sleep(0.5)
