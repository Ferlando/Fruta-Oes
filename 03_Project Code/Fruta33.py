#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from ev3dev.ev3 import * #to allow the use of brick buttons
import math
import ColorSensor2
from time import sleep

#-----------------------------------------------------------------
#Device Connections start

# Connect the outputs to the motor
motor_left = ev3.LargeMotor('outA')
motor_right = ev3.LargeMotor('outD')
gripper_motor = ev3.MediumMotor('outC')

#Gyro Sensor initialisation
gy = ev3.GyroSensor()

#Colour Sensor initialisation
cl= ColorSensor2.ColorSensor2()
cl.mode='COL-COLOR'

#Ultra-Sonic Sensor initialisation
us = ev3.UltrasonicSensor() 
us.mode='US-DIST-CM'

btn = Button() #activate the use of brick buttons

#Global Variables (we know use of global variables is not a good practice, but in this case it is necessary)
harvested = 0  #keeping count of the harvested fruits
total_distance = 0  #keeping track of the distance travelled by the robot
gripper_opened = True   #keeping track of the state of the gripper
original_angle = gy.value() 

#Device Connections ends
#----------------------------------------------------------------


#----------------------------------------------------------------
#Functions in this block

def menu():
    ev3.Sound.speak("Select the colour from the buttons after the beep").wait()
    sleep(3)
    Sound.beep().wait()
    
    while True:
        if btn.any():# Checks if any button is pressed.
            button_id = btn.buttons_pressed
            print(button_id[0])
            break
        else:
            sleep(0.01)
            
    option_text = " I will search for {0}"
    ev3.Sound.speak(option_text.format(fruit_dict.get(button_id[0]))).wait() 
    print(fruit_dict.get(button_id[0])) 
    return fruit_dict.get(button_id[0])
#**********************************************
def straighten():
    if (gy.value()>original_angle):
        turn_left(50,gy.value()-original_angle)
    elif (gy.value() < original_angle):
        turn_right(50,original_angle - gy.value())

#**********************************************
def turn_left(speed,angle):
    gy.mode = 'GYRO-RATE'
    gy.mode = 'GYRO-ANG'
    sleep(1)
    while gy.value()>-angle:
        motor_left.run_forever(speed_sp=-speed, stop_action = 'hold')
        motor_right.run_forever(speed_sp=speed, stop_action = 'hold')
        #print(gy.value())
    motor_left.stop()
    motor_right.stop()
#**********************************************   
def turn_right(speed,angle):
    gy.mode = 'GYRO-RATE'
    gy.mode = 'GYRO-ANG'
    sleep(1)
    while gy.value()<angle:
        motor_left.run_forever(speed_sp=speed, stop_action = 'hold')
        motor_right.run_forever(speed_sp=-speed, stop_action = 'hold')
        #print(gy.value())
    motor_left.stop()
    motor_right.stop()
#**********************************************

def move_distance_in_mm(distance_mm):
    dist = (distance_mm/1000) * (360/0.176)
    #print(dist)
    motor_left.run_to_rel_pos(position_sp = dist, speed_sp=400, stop_action = "brake")
    motor_right.run_to_rel_pos(position_sp = dist, speed_sp=400, stop_action = "brake")
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.stop()
    motor_right.stop()
#**********************************************
def drive_to_home_zone(hypotenuse, current_angle, add):
    global total_distance, harvested
    distance = abs(hypotenuse*(math.sin(math.radians(current_angle))))
    total_distance += abs(hypotenuse*(math.cos(math.radians(current_angle))))
    #print(distance,"Home distance")
    #print(math.sin(math.radians(current_angle)),"that")
    turn_right(100,current_angle + 80)
    gy.mode = 'GYRO-RATE'
    gy.mode = 'GYRO-ANG'
    sleep(1)
    move_distance_in_mm(abs(distance + add))
    gripper("open")
    harvested += 1  #keeping count of the harvested fruits
    move_distance_in_mm(-add)
    turn_left(200,70)
    print(gy.value(),"Home to zone")

#**********************************************
def drive_from_acre_to_line(hypotenuse, current_angle):
    global total_distance
    distance = abs(hypotenuse*(math.sin(math.radians(current_angle))))
    print(distance)
    turn_left(1000, 80)
    turn_right(200,current_angle)
    total_distance += abs(hypotenuse*(math.cos(math.radians(current_angle))))
    #print(distance,"Home distance")
    #print(math.sin(math.radians(current_angle)),"that")
    
    #turn_right(100,current_angle + 80)
    print(gy.value(),"Acre to line")
    gy.mode = 'GYRO-RATE'
    gy.mode = 'GYRO-ANG'
    sleep(1)
    move_distance_in_mm(-abs(distance))
    
#**********************************************

#**********************************************

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

#**********************************************

#**********************************************
def scanning():
    global total_distance
    gy.mode = 'GYRO-RATE'
    gy.mode = 'GYRO-ANG'
    sleep(1)
    search_space = 1300
    scanning_speed = 50
    dist = us.value()
    while(dist > search_space):
        while(dist > search_space and gy.value()>-80): # its suppose to be -90 but i put -75 because gyro is not accurate
            #print(dist)
            motor_left.run_forever(speed_sp=-scanning_speed, stop_action = 'hold')
            motor_right.run_forever(speed_sp=scanning_speed, stop_action = 'hold')
            dist = us.value()
        motor_left.stop()
        motor_right.stop()
        
        while(dist > search_space and gy.value()<-10):
            #print(dist)
            motor_left.run_forever(speed_sp=scanning_speed, stop_action = 'hold')
            motor_right.run_forever(speed_sp=-scanning_speed, stop_action = 'hold')
            dist = us.value()
        motor_left.stop()
        motor_right.stop()
        
        thetha = gy.value()
        dist =us.value()
        #print(us.value(),thetha,"thetha")  
        if(dist > search_space):
            move_distance_in_mm(200)
            total_distance += 200

    while(us.value() < search_space):# and gy.value()>-90):
        motor_left.run_forever(speed_sp=-50, stop_action = 'hold')
        motor_right.run_forever(speed_sp=50, stop_action = 'hold')    
    motor_left.stop()
    motor_right.stop()
    #current_angle = gy.value()
    alpha = gy.value() - thetha
    #print(us.value(),gy.value(),"gy.value")
    #print(us.value(),alpha,"alpha")

    while (gy.value()< (thetha + (alpha/2))):
        motor_left.run_forever(speed_sp=50, stop_action = 'hold')
        motor_right.run_forever(speed_sp=-50, stop_action = 'hold')
    motor_left.stop()
    motor_right.stop()
    
    #approaching
    #print(dist,"Disance to move")
    #print(gy.value(),"Angle of object")
    move_distance_in_mm(dist+10)
    sleep(1)
    gripper('close')
    #gripper.run_to_rel_pos(speed_sp=150, position_sp=230, stop_action = 'brake') # closing
    #gripper.wait_while('running')
    #sleep(3)
    if (cl.getCalibratedColorString() == fruit):
        ev3.Sound.speak("Right")
        drive_to_home_zone(dist, abs(gy.value()), 300)
        gripper('open') #this can be done in the main code
    else:
        ev3.Sound.speak("wrong")
        gripper('open') #this can be done in the main code
        #turn_left(200,80)
        #turn_right(200,80)
        #gy.mode = 'GYRO-RATE'
        #gy.mode = 'GYRO-ANG'
        #sleep(1)
        #move_distance_in_mm(-250)
        print(dist, "Distance")
        drive_from_acre_to_line(dist, abs(gy.value()))    
        #move_distance_in_mm(-abs(300))
        turn_right(200,80)
        #move_distance_in_mm(150)
        #total_distance += 150
    
    # if (us.value() > 1000) and (gy.value()<-90):
        # while(us.value() > 1000) and (gy.value()<0):
            # motor_left.run_forever(speed_sp=100, stop_action = 'hold')
            # motor_right.run_forever(speed_sp=-100, stop_action = 'hold')
        # motor_left.stop()
        # motor_right.stop()
#No Function definition below this line
#----------------------------------------------------------------

#Main Code

#Disctionary of all possible fruits (Coloured cubes) in the competition and corresponding selection button 

fruit_dict ={   #Declaring the available fruits
    'up':"Red",
    "right":"Green",
    "left":"Blue",
    "down":"Yellow",
}

motor_left.stop()
motor_right.stop()


#gripper('open')
#fruit = menu() #Fruit to be harversted WORKING

#while (harvested<1):
    #scanning()
#scanning()
#move_distance_in_mm(-total_distance)

#scanning()
