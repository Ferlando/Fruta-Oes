#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep
# let one wheel of the Marsrover move foreward

# Connect the outputs to the motor
motor_left = ev3.LargeMotor('outC')
motor_right = ev3.LargeMotor('outB')

#Gyro Sensor
gy = ev3.GyroSensor()

def move_distance(distance_cm):
    dist = (distance_cm/100) * (360/0.176)
    print(dist)
    motor_left.run_to_rel_pos(position_sp = dist, speed_sp=250, stop_action = "brake")
    motor_right.run_to_rel_pos(position_sp = dist, speed_sp=250, stop_action = "brake")
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.stop()
    motor_right.stop()
    
def turn_left():
    gy.mode = 'GYRO-RATE'
    gy.mode = 'GYRO-ANG'
    ev3.Sound.speak("Turning left")
    while gy.value()>-90:
        motor_left.run_forever(speed_sp=-200, stop_action = 'hold')
        motor_right.run_forever(speed_sp=200, stop_action = 'hold')
        #ev3.Sound.beep()
        print(gy.value())
    motor_left.stop()
    motor_right.stop()
    
def turn_right():
    gy.mode = 'GYRO-RATE'
    gy.mode = 'GYRO-ANG'
    ev3.Sound.speak("Turning right")
    while gy.value()<90:
        motor_left.run_forever(speed_sp=200, stop_action = 'hold')
        motor_right.run_forever(speed_sp=-200, stop_action = 'hold')
        #ev3.Sound.beep()
        print(gy.value())
    motor_left.stop()
    motor_right.stop()
    
#while gy.value()<90:
#    motor_left.run_forever(speed_sp=200)
#    motor_right.run_forever(speed_sp=-200)
#    ev3.Sound.beep()
move_distance(25)
turn_left()
move_distance(25)
turn_right()
	
for i in range(3):
    move_distance(50)
    turn_right()
    i=i+1
move_distance(25)
turn_left()
move_distance(25)
#print(gy.value())
ev3.Sound.speak("task complete")
sleep(1)
