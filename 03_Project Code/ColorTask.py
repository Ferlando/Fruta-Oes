#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import ColorSensor2
from time import sleep
# let one wheel of the Marsrover move foreward

# Connect the outputs to the motor
motor_left = ev3.LargeMotor('outC')
motor_right = ev3.LargeMotor('outB')

#cl=ev3.ColorSensor()
cl= ColorSensor2.ColorSensor2()
cl.mode='COL-COLOR'




def move_color(distance_cm):
    dist = (distance_cm/100) * (360/0.176)
    print(dist)
    
    dist2 = (1/100) * (360/0.176)
    dist3 = (16/100) * (360/0.176)
    ac=0
    while(ac<distance_cm):
        
        motor_right.run_to_rel_pos(position_sp = dist2, speed_sp = 250, stop_action = "brake")
        motor_left.run_to_rel_pos(position_sp = dist2, speed_sp = 250, stop_action = "brake")
        motor_right.wait_while('running')
        motor_left.wait_while('running')
        if(cl.value() != 0):
            motor_right.stop()
            motor_left.stop()
            ev3.Sound.speak(cl.getCalibratedColorString())
            ac = ac+16
            
            motor_right.run_to_rel_pos(position_sp = dist3, speed_sp = 250, stop_action = "brake")
            motor_left.run_to_rel_pos(position_sp = dist3, speed_sp = 250, stop_action = "brake")
            motor_right.wait_while('running')
            motor_left.wait_while('running')

        ac = ac+1
        
        print("ac", ac)
        
    motor_right.stop()
    motor_left.stop()

move_color(100)