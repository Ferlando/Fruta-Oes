#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep
# let one wheel of the Marsrover move foreward

# Connect the outputs to the motor
motor_left = ev3.LargeMotor('outC')
motor_right = ev3.LargeMotor('outB')

#Gyro Sensor
gy = ev3.GyroSensor()

gy.mode= 'GYRO-RATE'
gy.mode= 'GYRO-ANG'

while   gy.value()<180:
    motor_left.run_forever(speed_sp=200, stop_action = 'hold')
    motor_right.run_forever(speed_sp=-200, stop_action = 'hold')
    ev3.Sound.beep()

motor_left.stop()
motor_right.stop()
ev3.Sound.speak("180 degree turn complete")
sleep(1)

