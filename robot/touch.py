#!/usr/bin/env python
# encoding: utf-8

from ev3.lego import TouchSensor
from time import sleep

d = TouchSensor()
while 1:
    if (d.is_pushed):
        print "ok"

    sleep(0.3)
