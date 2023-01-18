#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from time import sleep

# New class for optimized color detection
# You can use the sensor class ColorSensor2 as follows:
# import ColorSensor2")
# cs2 = ColorSensor2.ColorSensor2()")
# cs2.getCalibratedColor() # color number")
# cs2.getCalibratedColorString() # color name")
# The first time you call it, it may require a recalibration.
# Therefor read the description for function recalibrate_sensor()
class ColorSensor2(ev3.ColorSensor):
    DEFAULT_SCALE = [209, 226, 207]
    """ Base Class """
    __slots__ = ['auto_mode']
    def __init__(self, address=None, name_pattern=ev3.ColorSensor.SYSTEM_DEVICE_NAME_CONVENTION, name_exact=False, **kwargs):
        super(ev3.ColorSensor, self).__init__(address, name_pattern, name_exact, driver_name=['lego-ev3-color'], **kwargs)
        self.auto_mode = True
        try:
            file = open("cal_values.txt", "r")
            self.DEFAULT_SCALE[0] = int(file.readline())
            self.DEFAULT_SCALE[1] = int(file.readline())
            self.DEFAULT_SCALE[2] = int(file.readline())
            file.close()
        except:
            self.recalibrate_sensor()
    
    # Return the raw RGB values. Useful for calibrating. Hold the sensor approx. 1cm over a white surface and call this function.
    # Note the returned values. You will need them for the function getCalibratedColor()
    def getScale(self):
        return self.raw
        
    # Return the detected color that uses an improved algorithm
    # You need the calibration values (scale) you get from getScale() while a white surface is in front of sensor
    def getCalibratedColor(self, scale = DEFAULT_SCALE):
        # Get a tuple of all 3 base color values
        rgb_raw = self.raw
        # Calculate HSV
        hsv = self.calcHSV(rgb_raw, scale)
        return self.color2(hsv)
    
    """ This function recalibrates the sensor.
        The current calibration values are valid for the sensor that comes with your box.
        If you get a new sensor or one from another team, you have to recalibrate the new sensor.
        Execute this function once with python3 and follow the guidance.
        The function simply gets the RGB values while you hold the sensor above a white surface (e.g. paper).
        It stores the calibration data into a file named 'cal_values.txt'.
        Do not delete this file when you want to use the new ColorSensor2 class.
    """
    # Update calibration file
    def recalibrate_sensor(self):
        # Guidance
        input("Hold the sensor approx. 1cm over a white surface and press ENTER!")

        # Get current RGB values
        scale = self.getScale()
        print("Scale for this sensor is: " + str(scale))

        # Store the values in current member variable
        self.DEFAULT_SCALE[0] = scale[0]
        self.DEFAULT_SCALE[1] = scale[1]
        self.DEFAULT_SCALE[2] = scale[2]

        # Store the values into the file 'cal_values.txt'
        file = open("cal_values.txt", "w+")
        file.write(str(scale[0])+"\n")
        file.write(str(scale[1])+"\n")
        file.write(str(scale[2])+"\n")
        file.close()

        # Final message
        print("Scale file successfully written.")
        print("You can use the sensor class ColorSensor2 now:")
        print("import ColorSensor2")
        print("cs2 = ColorSensor2.ColorSensor2()")
        print("cs2.getCalibratedColor() # color number")
        print("cs2.getCalibratedColorString() # color name")

    # Update calibration file
    def recalibrate_sensor_mean(self):
        # Guidance
        print("There will be 10 measurements - one each 1s.")
        input("Move the sensor approx. 1cm over a white surface and press ENTER!")

        # Prepare array for 10 measurements
        redValues = [0,0,0,0,0,0,0,0,0,0]
        greenValues = [0,0,0,0,0,0,0,0,0,0]
        blueValues = [0,0,0,0,0,0,0,0,0,0]
        
        for i in range(10):
            # Get current RGB values
            scale = self.getScale()
            print("Scale for this sensor is: " + str(scale))
            redValues[i] = scale[0]
            greenValues[i] = scale[1]
            blueValues[i] = scale[2]
            sleep(1)

        # Store the values in current member variable
        #print(redValues)
        #print(greenValues)
        #print(blueValues)
        self.DEFAULT_SCALE[0] = int((redValues[0] + redValues[1] + redValues[2] + redValues[3] + redValues[4] + redValues[5] + redValues[6] + redValues[7] + redValues[8] + redValues[9]) / 10)
        self.DEFAULT_SCALE[1] = int((greenValues[0] + greenValues[1] + greenValues[2] + greenValues[3] + greenValues[4] + greenValues[5] + greenValues[6] + greenValues[7] + greenValues[8] + greenValues[9]) / 10)
        self.DEFAULT_SCALE[2] = int((blueValues[0] + blueValues[1] + blueValues[2] + blueValues[3] + blueValues[4] + blueValues[5] + blueValues[6] + blueValues[7] + blueValues[8] + blueValues[9]) / 10)

        # Store the values into the file 'cal_values.txt'
        file = open("cal_values.txt", "w+")
        file.write(str(self.DEFAULT_SCALE[0])+"\n")
        file.write(str(self.DEFAULT_SCALE[1])+"\n")
        file.write(str(self.DEFAULT_SCALE[2])+"\n")
        file.close()

        # Final message
        print("Scale file successfully written.")
        print("You can use the sensor class ColorSensor2 now:")
        print("import ColorSensor2")
        print("cs2 = ColorSensor2.ColorSensor2()")
        print("cs2.getCalibratedColor() # color number")
        print("cs2.getCalibratedColorString() # color name")

    # Identifies a color from the hsv values.
    # The range of the hsv array must be (0,1)
    # Returns a color as a string
    # Takes the hsv values as 3-dimensional array with values in range (0,1)
    def getCalibratedColorString(self, scale = DEFAULT_SCALE):
        return self.COLORS[self.getCalibratedColor(scale)]

    # Identifies a color from the hsv values.
    # The range of the hsv array must be (0,1)
    # Returns a color number
    # Takes the hsv values as 3-dimensional array with values in range (0,1)
    def color2(self, hsv):
        color = 0 #no color
        if hsv[0] == None:
            if hsv[2] < 0.15:
                color = 1 #black
            elif hsv[2] > 0.9 and hsv[1] < 0.1:
                color = 6 #white
            else:
                color = 8 #grey
        else:
            if hsv[2] < 0.15:
                color = 1 #black
            elif hsv[2] > 0.8 and hsv[1] < 0.3:
                color = 6 #white
            elif hsv[0] > 170 and hsv[0] <= 265:
                color = 2 #blue
            elif hsv[0] > 80 and hsv[0] <= 170:
                color = 3 #green
            elif hsv[0] > 10 and hsv[0] <= 32:
                color = 7 #brown
            elif hsv[0] > 40 and hsv[0] <= 80:
                color = 4 #yellow
            elif hsv[0] > 330 or hsv[0] <= 40:
                color = 5 #red
        return color
    
    # Convert a rgb array to hsv array
    # Returns the hsv array with values in range (0,1)
    # Takes parameters:
    # rgb: A 3-dimensional array containing the values for red, green and blue channel
    # scale: A 3-dimensional array containing the maximum values possible for each channel
    def calcHSV(self, rgb, scale = DEFAULT_SCALE):
        # scale rgb to range 0...1
        r = rgb[0] / scale[0]
        g = rgb[1] / scale[1]
        b = rgb[2] / scale[2]
        # get the maximum and minimum
        mx = max(r, g, b)
        mn = min(r, g, b)
        # calculate H value 0...360° or None for white...grey...black
        if mn == mx:
            h = None
        elif mx == r:
            h = 60 * (0 + (g-b) / (mx-mn))
        elif mx == g:
            h = 60 * (2 + (b-r) / (mx-mn))
        elif mx == b:
            h = 60 * (4 + (r-g) / (mx-mn))
        if h != None and h < 0:
            h = h + 360
        # calculate S value
        if mx == 0:
            s = 0
        else:
            s = (mx-mn)/mx
        # calculate V value
        v = mx
        hsv = (h, s, v)
        return hsv
