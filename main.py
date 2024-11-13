#!/usr/bin/env python3

from time import sleep
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import LightSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from BotCode.lightSensor import *
from BotCode.drive import *

speed = 50
coursCompleted = False
eventCounter = 1

leftSensor = LightSensor(INPUT_1)
middleSensor = LightSensor(INPUT_2)
rightSensor = LightSensor(INPUT_3)
distanceSensor = UltrasonicSensor(INPUT_4)

threshold = recalibrate()

print(distanceSensor.distance_centimeters)

while not coursCompleted:
    if distanceSensor.distance_centimeters > 10:
        if leftSensor.reflected_light_intensity < lsThreshold:
            turnLeft(speed, speed)
        elif rightSensor.reflected_light_intensity < lsThreshold:
            turnRight(speed, speed)
        else:
            forward(speed)
    elif distanceSensor.distance_centimeters <= 10 and eventCounter == 1:
        turn180OnSpot()
        eventCounter += 1
    elif distanceSensor.distance_centimeters <= 10 and eventCounter == 2:
        stop()
        while distanceSensor.distance_centimeters <= 20:
            sleep(5)
        eventCounter += 1
    elif distanceSensor.distance_centimeters <= 20 and eventCounter == 4:  # and all sensors black
        pass
        # throw ball
    else:
        coursCompleted = True

# Sunaa Risu
