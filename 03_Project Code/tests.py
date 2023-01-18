#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import ColorSensor2
from os import system, name 
from time import sleep, time


# define our clear function to clear the screen
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def printcolors(colors, colorcounter):
    clear()
    for i in range(8):
        print(colors[i]+'\t'+str(colorcounter[i]))

def calibrate_colorsensor():
    clear()
    cs = ColorSensor2.ColorSensor2()
    answer = input("One (1) or ten (10) measurements? ")
    if answer == "1":
        cs.recalibrate_sensor()
    else:
        cs.recalibrate_sensor_mean()
    input("Sensor calibrated. Press ENTER.")

def test_colorsensor():
    success = True
    try:
        colors = ["no color", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]
        for i in range(1, 8):
            try:
                input("Place the sensor approximately 1cm over a " + colors[i] + " surface and press ENTER")
                correctcounter = 0
                incorrectcounter = 0
                for j in range(100):
                    cs = ColorSensor2.ColorSensor2()
                    color = cs.getCalibratedColorString()
                    if color == colors[i]:
                        correctcounter += 1
                    else:
                        incorrectcounter += 1
                    #print(color + " -> " + str(correctcounter))
                print("Precision is " + str(correctcounter) + "%")
                if correctcounter < 95:
                    success = False
            except:
                print("Test cancelled. Press ENTER.")
                input("")
                return False
        input("Test finished. Press ENTER.")
    except:
        print("Connect sensor before starting the test. Press ENTER.")
        input("")
        return False
    return success

def test_gyro_sensor():
    success = True
    try:
        gs = ev3.GyroSensor()
        gs.mode = 'GYRO-ANG'
        print("Starting test in 5s.")
        sleep(2)
        gs.mode = 'GYRO-RATE'
        sleep(1)
        gs.mode = 'GYRO-ANG'
        sleep(2)
        try:
            input("Rotate counterclockwise to -90 degrees and press ENTER.")
            angle = gs.value()
            print("Angle: " + str(angle))
            if angle < -93 or angle > -87:
                success = False
            input("Rotate counterclockwise to -180 degrees and press ENTER.")
            angle = gs.value()
            print("Angle: " + str(angle))
            if angle < -183 or angle > -177:
                success = False
            input("Rotate counterclockwise to -360 degrees and press ENTER.")
            angle = gs.value()
            print("Angle: " + str(angle))
            if angle < -363 or angle > -357:
                success = False
            input("Rotate clockwise back to 0 degrees and press ENTER.")
            angle = gs.value()
            print("Angle: " + str(angle))
            if angle < -3 or angle > 3:
                success = False
            if success:
                input("Test successful. Press ENTER.")
            else:
                input("Test failed. Press ENTER.")
        except:
            print("Test cancelled. Press ENTER.")
            input("")
            return False
    except:
        print("Connect sensor before starting the test. Press ENTER.")
        input("")
        return False
    return success

def test_touch_sensor():
    success = True
    try:
        touch = ev3.TouchSensor()
        dummy = touch.value()
        print("Test started - press touch sensor within 2 seconds")
        start = time()
        while not touch.value():
            pass
        ev3.Sound.beep()
        if time() - start > 2:
            input("Test failed. Press ENTER")
            success = False
        else:
            input("Test successful. Press ENTER")
    except:
        print("Connect sensor before starting the test. Press ENTER.")
        input("")
        success = False
    return success

def test_ultrasonic_sensor():
    success = True
    try:
        us = ev3.UltrasonicSensor()
        us.mode = 'US-DIST-CM'
        input("Point the sensor to a wall far away and press ENTER.")
        print("Distance: " + str(us.value()/10.0) + " cm")
        input("Now try to adjust a distance of 1 meter. Press ENTER as soon as you are ready.")
        dist = us.value()/10.0
        while dist < 95 or dist > 105:
            sleep(0.25)
            print("Distance: " + str(dist) + " cm")
            dist = us.value()/10.0
        print("Distance: " + str(dist) + " cm")
        input("Now try to adjust a distance of 20cm. Press ENTER as soon as you are ready.")
        while dist < 18 or dist > 22:
            sleep(0.25)
            print("Distance: " + str(dist) + " cm")
            dist = us.value()/10.0
        print("Distance: " + str(dist) + " cm")
        input("Now try to adjust a distance of 5cm. Press ENTER as soon as you are ready.")
        while dist < 4 or dist > 6:
            sleep(0.25)
            print("Distance: " + str(dist) + " cm")
            dist = us.value()/10.0
        print("Distance: " + str(dist) + " cm")
        input("Test successful. Press ENTER")
    except:
        input("Connect sensor before starting the test. Press ENTER.")
        success = False
    return success

def test_motor(motor, tolerances):
    success = True
    print("Start test")
    
    # 1) run_timed slow, medium, high speed
    print("run_timed 1s each 100, 500, 1000 deg/s")
    sleep(1)
    start = motor.position
    motor.run_timed(time_sp=1000, speed_sp=100)
    motor.wait_while('running')
    end = motor.position
    print(" rotation angle: ", end-start)
    if abs(end-start-100) > tolerances[0]:
        success = False
        print("Test failed")
    sleep(1)
    start = motor.position
    motor.run_timed(time_sp=1000, speed_sp=500)
    motor.wait_while('running')
    end = motor.position
    print(" rotation angle: ", end-start)
    if abs(end-start-500) > tolerances[1]:
        success = False
        print("Test failed")
    sleep(1)
    start = motor.position
    motor.run_timed(time_sp=1000, speed_sp=1000)
    motor.wait_while('running')
    end = motor.position
    print(" rotation angle: ", end-start)
    if abs(end-start-1000) > tolerances[2]:
        success = False
        print("Test failed")
    
    # 2) run_timed reverse slow, medium, high speed
    print("run_timed reverse 1s each 100, 500, 1000 deg/s")
    sleep(1)
    start = motor.position
    motor.run_timed(time_sp=1000, speed_sp=-100)
    motor.wait_while('running')
    end = motor.position
    print(" rotation angle: ", end-start)
    if abs(end-start+100) > tolerances[3]:
        success = False
        print("Test failed")
    sleep(1)
    start = motor.position
    motor.run_timed(time_sp=1000, speed_sp=-500)
    motor.wait_while('running')
    end = motor.position
    print(" rotation angle: ", end-start)
    if abs(end-start+500) > tolerances[4]:
        success = False
        print("Test failed")
    sleep(1)
    start = motor.position
    motor.run_timed(time_sp=1000, speed_sp=-1000)
    motor.wait_while('running')
    end = motor.position
    print(" rotation angle: ", end-start)
    if abs(end-start+1000) > tolerances[5]:
        success = False
        print("Test failed")
    
    # 3) rotate by 90 degrees
    print("rotate by 90 degrees")
    sleep(1)
    start = motor.position
    motor.run_to_rel_pos(position_sp=90, speed_sp=100)
    motor.wait_while('running')
    end = motor.position
    print(" rotation angle: ", end-start)
    if abs(end-start-90) > tolerances[6]:
        success = False
        print("Test failed")
    
    # 4) rotate by 180 degrees
    print("rotate by 180 degrees")
    sleep(1)
    start = motor.position
    motor.run_to_rel_pos(position_sp=180, speed_sp=100)
    motor.wait_while('running')
    end = motor.position
    print(" rotation angle: ", end-start)
    if abs(end-start-180) > tolerances[7]:
        success = False
        print("Test failed")
    
    # 5) rotate by -360 degrees
    print("rotate by -360 degrees")
    sleep(1)
    start = motor.position
    motor.run_to_rel_pos(position_sp=-360, speed_sp=100)
    motor.wait_while('running')
    end = motor.position
    print(" rotation angle: ", end-start)
    if abs(end-start+360) > tolerances[8]:
        success = False
        print("Test failed")
    
    # 6) stop action hold
    print("stop action hold")
    sleep(1)
    motor.run_forever(speed_sp=1000)
    sleep(3)
    motor.stop(stop_action="hold")
    start = motor.position
    sleep(1)
    end = motor.position
    print(" rotation angle: ", end-start)
    if abs(end-start) > tolerances[9]:
        success = False
        print("Test failed")
    
    # 7) stop action coast
    print("stop action coast")
    sleep(1)
    motor.run_forever(speed_sp=1000)
    sleep(3)
    motor.stop(stop_action="coast")
    start = motor.position
    sleep(3)
    end = motor.position
    print(" rotation angle: ", end-start)
    if abs(end-start) > tolerances[10]:
        success = False
        print("Test failed")
    
    # 8) stop action brake
    print("stop action brake")
    sleep(1)
    motor.run_forever(speed_sp=1000)
    sleep(3)
    motor.stop(stop_action="brake")
    start = motor.position
    sleep(1)
    end = motor.position
    print(" rotation angle: ", end-start)
    if abs(end-start) > tolerances[11]:
        success = False
        print("Test failed")

    return success
    
def test_large_motor():
    tolerances = [20, 40, 300, 20, 40, 300, 2, 2, 2, 2, 800, 70]
    success = True
    try:
        largemotor = ev3.LargeMotor()
        dummy = largemotor.position
        try:
            success = test_motor(largemotor, tolerances)
        except:
            print("Test aborted")
            return False
        if success:
            input("Test successful. Press ENTER")
        else:
            input("Test failed. Press ENTER")
        return success
    except:
        print("Connect motor before starting the test. Press ENTER.")
        input("")
        return False

def test_medium_motor():
    tolerances = [20, 40, 150, 20, 40, 150, 2, 2, 2, 2, 100, 40]
    success = True
    try:
        mediummotor = ev3.MediumMotor()
        dummy = mediummotor.position
        try:
            success = test_motor(mediummotor, tolerances)
        except:
            print("Test aborted")
            return False
        if success:
            input("Test successful. Press ENTER")
        else:
            input("Test failed. Press ENTER")
        return success
    except:
        print("Connect motor before starting the test. Press ENTER.")
        input("")
        return False

# print the main menu
def printmenu():
    clear()
    print("Select test and press ENTER or any other input to exit:")
    print("0:  Color sensor calibration")
    print("1:  Color sensor")
    print("2:  Gyro sensor")
    print("3:  Touch sensor")
    print("4:  Ultrasonic sensor")
    print("5:  Large motor")
    print("6:  Medium motor")
    print("x:  exit program")
    print("-----------------------------")
    
# main loop for all tests
try:
    file = open("tests.log", "w+")
    while True:
        printmenu()
        selection = input("")
        if selection == "0":
            calibrate_colorsensor()
        if selection == "1":
            if test_colorsensor():
                file.write("Test of color sensor SUCCESSFUL\n")
            else:
                file.write("Test of color sensor FAILED\n")
        if selection == "2":
            if test_gyro_sensor():
                file.write("Test of gyro sensor SUCCESSFUL\n")
            else:
                file.write("Test of gyro sensor FAILED\n")
        if selection == "3":
            if test_touch_sensor():
                file.write("Test of touch sensor SUCCESSFUL\n")
            else:
                file.write("Test of touch sensor FAILED\n")
        if selection == "4":
            if test_ultrasonic_sensor():
                file.write("Test of ultrasonic sensor SUCCESSFUL\n")
            else:
                file.write("Test of ultrasonic sensor FAILED\n")
        if selection == "5":
            if test_large_motor():
                file.write("Test of large motor SUCCESSFUL\n")
            else:
                file.write("Test of large motor FAILED\n")
        if selection == "6":
            if test_medium_motor():
                file.write("Test of medium motor SUCCESSFUL\n")
            else:
                file.write("Test of medium motor FAILED\n")
        if selection == "x":
            break
finally:
    file.close()
