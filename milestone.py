#!/usr/bin/env python3

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import LightSensor, ColorSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from BotCode.lightSensor import *
from BotCode.drive import *
from math import pi

SPEED = -20  # negativ because the motors are mounted backwards -__-
TIRE_DIAMETER = 0.1  # diameter in si units
METER_PER_SECONDS = TIRE_DIAMETER * pi

coursCompleted = False
eventCounter = 1

leftSensor = LightSensor(INPUT_1)
middleSensor = LightSensor(INPUT_2)
rightSensor = LightSensor(INPUT_3)
distanceSensor = UltrasonicSensor(INPUT_4)

threshold = calibration()

print(distanceSensor.distance_centimeters)

while not coursCompleted:
    if distanceSensor.distance_centimeters > 10:
        leftSensorLightIntensity = leftSensor.reflected_light_intensity
        rightSensorLightIntensity = rightSensor.reflected_light_intensity
        if type(leftSensor.reflected_light_intesity) is not int:
            leftSensorLightIntensity = 255
        if type(right.reflected_light_intesity) is not int:
            rightSensorLightIntensity = 255
        if leftSensor.reflected_light_intensity < threshold:
            turnLeft(SPEED, SPEED)
        elif rightSensor.reflected_light_intensity < threshold:
            turnRight(SPEED, SPEED)
        else:
            forward(SPEED)
    elif distanceSensor.distance_centimeters <= 10 and eventCounter == 1:
        turn180OnSpot()
        eventCounter += 1
    else:
        stop()
        coursCompleted = True

# Sunaa Risu
