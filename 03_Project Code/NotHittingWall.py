#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep
# let one wheel of the Marsrover move foreward

# Connect the outputs to the motor
motor_left = ev3.LargeMotor('outB')
motor_right = ev3.LargeMotor('outC')

us = ev3.UltrasonicSensor() 
us.mode='US-DIST-CM'
ts = ev3.TouchSensor() # connect a touch sensor anywhere


def move_wall():
    dist2 = (200/100) * (360/0.176)
    
    while not ts.value(): # loop if the button is not pressed
        sleep(0.01) 
    
    while(us.value()>70):

        motor_right.run_to_rel_pos(position_sp = dist2, speed_sp = 1000, stop_action = "brake")
        motor_left.run_to_rel_pos(position_sp = dist2, speed_sp = 1000, stop_action = "brake")     
        print(us.value())
                      
    motor_right.stop()
    motor_left.stop()

move_wall()