#!/usr/bin/env python3

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import LightSensor, ColorSensor
from BotCode.lightSensor import initialCalibration
from BotCode.drive import forward, turnLeft, turnRight, stop

leftSensor = LightSensor(INPUT_1)
middleSensor = ColorSensor(INPUT_2)
rightSensor = LightSensor(INPUT_3)

calibrationData = initialCalibration()
lsThreshold = calibrationData[0]
csThreshold = calibrationData[1]

while True:
    if leftSensor.reflected_light_intensity < lsThreshold:
        turnLeft(100, 50)
    elif rightSensor.reflected_light_intensity < lsThreshold:
        turnRight(100, 50)
    else:
        forward(100)
