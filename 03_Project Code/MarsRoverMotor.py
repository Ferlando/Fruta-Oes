#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep
# let one wheel of the Marsrover move foreward

# Connect the output D to the motor
motor_left = ev3.LargeMotor('outC')
# move motor for 1000ms with 500dec/sec
motor_left.run_timed(time_sp=1000, speed_sp=500)
# wait till the motor has stopped
motor_left.wait_while('running')
ev3.Sound.speak("Hello World")
sleep(1)

