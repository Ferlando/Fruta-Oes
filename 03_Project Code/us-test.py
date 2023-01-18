#!/usr/bin/env python3
import ev3dev.ev3 as ev3
us = ev3.UltrasonicSensor() 
us.mode='US-DIST-CM'
while True:
    print(us.value())
