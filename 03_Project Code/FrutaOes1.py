#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
import ColorSensor2
from time import sleep

#-----------------------------------------------------------------
#Device Connections start

# Connect the outputs to the motor
motor_left = ev3.LargeMotor('outB')
motor_right = ev3.LargeMotor('outC')

#Gyro Sensor
gy = ev3.GyroSensor()

# Connect the touch sensors
#no_touch_sensor = ev3.TouchSensor('in2')
yes_touch_sensor = ev3.TouchSensor('in3')

#Colour Sensor 
#cl=ev3.ColorSensor()
cl= ColorSensor2.ColorSensor2()
cl.mode='COL-COLOR'


us = ev3.UltrasonicSensor() 
us.mode='US-DIST-CM'

#btn = Button()
#Device Connections ends
#----------------------------------------------------------------


#----------------------------------------------------------------
#Functions in this block


#No Function definition below this line
#----------------------------------------------------------------

#Main Code

#fruits = ["Blue", "Yellow", "Red", "Green"] #List of all possible fruits (Coloured cubes) in the competition
#event = threading.Event()
btn = Button() #activate the use of brick buttons

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
# def menu():

    # ev3.Sound.speak("Listen to the color menu and select after the beep").wait()
    # sleep(3)

    # for x, y in fruit_dict.items():
        # option_text = " Press {0} button for color {1} "
        # ev3.Sound.speak(option_text.format(x,y)).wait()
        # sleep(3)
    # Sound.beep().wait()
    
    # while True:
        # if btn.any():# Checks if any button is pressed.
            # button_id = btn.buttons_pressed
            # print(button_id[0])
            # break
        # else:
            # sleep(0.01)
            
    # option_text = " I will search for {0}"
    # ev3.Sound.speak(option_text.format(fruit_dict.get(button_id[0]))).wait() 
    # print(fruit_dict.get(button_id[0])) 
    # return fruit_dict.get(button_id[0])
# #**********************************************
# def menu():
    # option = False
    # fruits = [2, 3, 4, 5]
    
    # i = 0
    # ev3.Sound.speak("Show me the fruit to harvest")
    # sleep(2)
    # while (cl.value() == 1):
        # sleep(0.01)
    # while not option:
    # #for i in range(3):
        # cl.mode = 'COL-COLOR'
        
        # if(cl.value() in fruits):
            
            # option_text = "Is your colour {0}?"
            # ev3.Sound.speak(option_text.format(cl.getCalibratedColorString()))
            # ourcolour = cl.getCalibratedColorString()
            # while not yes_touch_sensor.value(): 
                # sleep(0.01)
                # if(yes_touch_sensor.value()):
                    # option_text = "I will search for {0}"
                    # ev3.Sound.speak(option_text.format(ourcolour))
                    # option = True
                    
                # elif(no_touch_sensor.value()):
                    
                    # break
            



def move_wall():
    dist2 = (200/100) * (360/0.176)
    
    while(us.value() > 700):
        
        motor_left.run_forever(speed_sp=-100, stop_action = 'hold')
        motor_right.run_forever(speed_sp=100, stop_action = 'hold')
    print(us.value(),"Spinning")
    motor_left.stop()
    motor_right.stop() 
    
    
    while(us.value()>70):
        motor_left.run_forever(speed_sp=200, stop_action = 'hold')
        motor_right.run_forever(speed_sp=200, stop_action = 'hold')    
        print(us.value(),"Approaching")
        
    print(us.value())                  
    motor_right.stop()
    motor_left.stop()

#gy.mode = 'GYRO-RATE'
#gy.mode = 'GYRO-ANG'
#menu()
def move_wall2():
    dist2 = (200/100) * (360/0.176)
    
    while(us.value() > 700):
        
        motor_left.run_forever(speed_sp=-100, stop_action = 'hold')
        motor_right.run_forever(speed_sp=100, stop_action = 'hold')
    print(us.value(),"Spinning")
    motor_left.stop()
    motor_right.stop() 
    
    last_value= us.value() + 1
    print(last_value,"initial value")
    while(us.value()>70):
        motor_left.run_forever(speed_sp=200, stop_action = 'hold')
        motor_right.run_forever(speed_sp=200, stop_action = 'hold')    
        print(us.value(),"Approaching")
        if(last_value<us.value()):
            motor_left.stop()
            motor_right.stop()
            print(us.value(),"US Value")
            gy.mode = 'GYRO-RATE'
            gy.mode = 'GYRO-ANG'
            print(us.value(),"US Value Updated")
            #print(last_value,"updated value2")
            #print(gy.value(),"Gyro hola")
            while gy.value()>-45 and us.value()>last_value:
                motor_left.run_forever(speed_sp=-100, stop_action = 'hold')
                motor_right.run_forever(speed_sp=100, stop_action = 'hold')
                print(us.value(),"Turning")
                print(gy.value(),"Gyro")
                last_value=us.value()
            motor_left.stop()
            motor_right.stop()
        last_value=us.value()
        print(last_value,"updated last value")
        
        
    print(us.value())                  
    motor_right.stop()
    motor_left.stop()

#move_wall2()

# while True:
    # if btn.any():
        # Sound.beep().wait()
        # exit()
    # else:
        # sleep(0.01)
        
# def left(state):
    # if state:
        # ev3.Sound.speak("Left pressed").wait()
    # else:
        # ev3.Sound.speak("Left released").wait()
        
# btn.on_left = left

# while True:
    # btn.process()
    # sleep(0.01)
    
# while True:
    # option_text = "{0}"
    # ev3.Sound.speak(option_text.format(btn.buttons_pressed)).wait()
    # #print(btn.buttons_pressed)
    # if btn.check_buttons(buttons = ['left','right']):
        # exit()
    # sleep(1)
    
def move_distance_in_mm(distance_mm):
    dist = (distance_mm/1000) * (360/0.176)
    print(dist)
    motor_left.run_to_rel_pos(position_sp = dist, speed_sp=250, stop_action = "brake")
    motor_right.run_to_rel_pos(position_sp = dist, speed_sp=250, stop_action = "brake")
    motor_left.wait_while('running')
    motor_right.wait_while('running')
    motor_left.stop()
    motor_right.stop()

def move_wall3():
    dist2 = (200/100) * (360/0.176)
    
    while(us.value() > 700):
        
        motor_left.run_forever(speed_sp=-100, stop_action = 'hold')
        motor_right.run_forever(speed_sp=100, stop_action = 'hold')
    print(us.value(),"Spinning")
    motor_left.stop()
    motor_right.stop() 
    
    gy.mode = 'GYRO-RATE'
    gy.mode = 'GYRO-ANG'
    while gy.value()>-20:#FERLNADO CHANGED THIS FROM -15 TO -20
        motor_left.run_forever(speed_sp=-10, stop_action = 'hold')
        motor_right.run_forever(speed_sp=10, stop_action = 'hold')
        print(gy.value())
    motor_right.stop()
    motor_left.stop()
    
    move_distance_in_mm(us.value()-10)#FERLNADO CHANGED THIS FROM -35 TO 10
    # distance = (us.value()/1000) * (360/0.176)
    
    # while(us.value()>70):
        # motor_left.run_forever(speed_sp=200, stop_action = 'hold')
        # motor_right.run_forever(speed_sp=200, stop_action = 'hold')    
        # print(us.value(),"Approaching")
        
    # print(us.value())                  
    # motor_right.stop()
    # motor_left.stop()
fruit_dict ={
    'up':"Red",
    "right":"Green",
    "left":"Blue",
    "down":"Yellow",
}

fruit = menu()   
move_wall3()
sleep(3)
if (cl.getCalibratedColorString() == fruit):
    ev3.Sound.speak("correct")
else:
    ev3.Sound.speak("wrong")
    
print(type(cl.getCalibratedColorString()))
print(type(fruit))
