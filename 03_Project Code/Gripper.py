#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from ev3dev.ev3 import * #to allow the use of brick buttons
import math
import ColorSensor2
from time import sleep

#-----------------------------------------------------------------

# Connect the outputs to the motor
gripper_motor = ev3.MediumMotor('outC')

#keeping track of the state of the gripper
gripper_opened = False   


#**********************************************
def gripper(command):
    global gripper_opened
    if (command == "close" and gripper_opened == True):
        gripper_motor.run_to_rel_pos(speed_sp=150, position_sp=230, stop_action = 'brake') # closing
        sleep(2)
        gripper_opened = False
    elif (command == "open" and gripper_opened == False):
        gripper_motor.run_to_rel_pos(speed_sp=250, position_sp=-210, stop_action = 'brake') #opening
        gripper_motor.wait_while('running')
        gripper_opened = True
#**********************************************


gripper('open')
#gripper('close')

