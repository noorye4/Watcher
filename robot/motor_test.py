#!/usr/bin/env python
# encoding: utf-8

from ev3.ev3dev import Motor
from ev3.lego import LargeMotor

# mL=Motor(port=Motor.PORT.A)
# mR=Motor(port=Motor.PORT.B)

motor_A = LargeMotor(port='A')
motor_B = LargeMotor(port='B')

motor_A.run_forever(500, speed_regulation=False)
