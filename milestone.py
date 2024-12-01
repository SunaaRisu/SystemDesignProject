#!/usr/bin/env python3

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import LightSensor, ColorSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sound import Sound
from BotCode.drive import *

SPEED = -20  # negativ because the motors are mounted backwards -__-
LIGHTOFFSET = 10
WALLDISTANCE = 10  # at which distance should the bot react to a wall

coursCompleted = False
eventCounter = 1  # counts to events on the track

leftSensor = LightSensor(INPUT_1)
middleSensor = LightSensor(INPUT_2)
rightSensor = LightSensor(INPUT_3)
distanceSensor = UltrasonicSensor(INPUT_4)
sound = Sound()

sound.beep()

while not coursCompleted:
    leftLight = leftSensor.reflected_light_intensity
    rightLight = rightSensor.reflected_light_intensity
    if distanceSensor.distance_centimeters > WALLDISTANCE:
        if (leftLight - LIGHTOFFSET < rightLight and rightLight - LIGHTOFFSET < leftLight) and ((leftLight + rightLight) / 2) > (middleSensor.reflected_light_intensity + LIGHTOFFSET):
            forward(SPEED)
        elif rightLight + LIGHTOFFSET < leftLight:
            turnRight(SPEED, SPEED)
        elif rightLight > leftLight + LIGHTOFFSET:
            turnLeft(SPEED, SPEED)
        else:
            forward(SPEED)
    elif distanceSensor.distance_centimeters <= WALLDISTANCE and eventCounter == 1:
        turn180()
        eventCounter += 1
    else:
        stop()
        coursCompleted = True

# Sunaa Risu
