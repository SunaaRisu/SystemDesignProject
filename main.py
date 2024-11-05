#!/usr/bin/env python3

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import LightSensor, ColorSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from BotCode.lightSensor import initialCalibration
from BotCode.drive import forward, turnLeft, turnRight, turn180, stop

speed = 20

leftSensor = LightSensor(INPUT_1)
middleSensor = ColorSensor(INPUT_2)
rightSensor = LightSensor(INPUT_3)
distanceSensor = UltrasonicSensor(INPUT_4)

calibrationData = initialCalibration()
lsThreshold = calibrationData[0]
csThreshold = calibrationData[1]

turn180()
print(lsThreshold)
print(csThreshold)
print(leftSensor.reflected_light_intensity)
print(rightSensor.reflected_light_intensity)
print(distanceSensor.distance_centimeters_ping)

while True:
    if leftSensor.reflected_light_intensity < lsThreshold:
        turnLeft(speed, speed)
    elif rightSensor.reflected_light_intensity < lsThreshold:
        turnRight(speed, speed)
    else:
        forward(speed)
