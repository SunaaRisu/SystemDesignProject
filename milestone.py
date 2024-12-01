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

print(distanceSensor.distance_centimeters)

while not coursCompleted:
    leftLight = leftSensor.reflected_light_intensity
    rightLight = rightSensor.reflected_light_intensity
    if distanceSensor.distance_centimeters > 10:
        if (leftLight - 10 < rightLight and rightLight - 10 < leftLight) and ((leftLight + rightLight) / 2) > (middleSensor.reflected_light_intensity + 10):
            forward(SPEED)
        elif rightLight < leftLight:
            turnRight(SPEED, SPEED)
        elif rightLight > leftLight:
            turnLeft(SPEED, SPEED)
        else:
            forward(SPEED)
    elif distanceSensor.distance_centimeters <= 10 and eventCounter == 1:
        turn180OnSpot()
        eventCounter += 1
    else:
        stop()
        coursCompleted = True

# Sunaa Risu
