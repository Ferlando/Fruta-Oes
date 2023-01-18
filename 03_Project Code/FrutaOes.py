#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import ev3dev2.sensor.lego.TouchSensor
import ColorSensor2
import signal, os
import threading
#import ev3dev.fonts as fonts
from time import sleep

#-----------------------------------------------------------------
#Device Connections start

# Connect the outputs to the motor
motor_left = ev3.LargeMotor('outB')
motor_right = ev3.LargeMotor('outC')

#Gyro Sensor
gy = ev3.GyroSensor()

# Connect the touch sensors
no_touch_sensor = ev3.TouchSensor('in2')
yes_touch_sensor = ev3.TouchSensor('in3')

#Colour Sensor 
#cl=ev3.ColorSensor()
cl= ColorSensor2.ColorSensor2()
cl.mode='COL-COLOR'

#Device Connections ends
#----------------------------------------------------------------


#----------------------------------------------------------------
#Functions in this block


#No Function definition below this line
#----------------------------------------------------------------

#Main Code

fruits = ["Blue", "Yellow", "Red", "Green"] #List of all possible fruits (Coloured cubes) in the competition
event = threading.Event()

def menu():
    option = False
    count = 0
    option_text = "Press Yes for {0} and No to continue"
    ev3.Sound.speak(option_text.format(fruits[count]))
    sleep(2)
    while yes_touch_sensor.value():

        #pressed = input("press the button")
        yes =  yes_touch_sensor.value()
        no = no_touch_sensor.value()
        print(yes)
        if yes:
            option_text = "You selected {0} press Yes or No"
            ev3.Sound.speak(option_text.format(fruits[count]))
            sleep(3)
            yes =  yes_touch_sensor.value()
            no = no_touch_sensor.value()
            
            if yes_touch_sensor.value():
                option_text = "I will search {0}"
                ev3.Sound.speak(option_text.format(fruits[count]))
                sleep(3)
                option = True
            else:
                option = False
        else:
            count += 1
            print(count)
  
    print(count)

menu()    

# print("Hello")
# var = input("enter value")
# print(var)
# while True:
    # if(cl.value() != 0):
        # ev3.Sound.speak(cl.getCalibratedColorString())
 
#sleep(1)
