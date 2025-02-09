#!/usr/bin/env python3

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import LightSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sound import Sound
from BotCode.drive import forward, turnLeft, turnRight, turn180, stop, throwBall

from time import sleep

SPEED = -20  # negativ because the motors are mounted backwards
LIGHTOFFSET = 8  # offset because sonsors are not calibrated very well
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
    left = leftSensor.reflected_light_intensity
    right = rightSensor.reflected_light_intensity
    middle = middleSensor.reflected_light_intensity
    leftCompare = left + LIGHTOFFSET
    rightCompare = right + LIGHTOFFSET
    middleCompare = middle + LIGHTOFFSET
    distance = distanceSensor.distance_centimeters

    if (distance <= WALLDISTANCE and eventCounter == 1):
        turn180()
        eventCounter = 2
        continue

    if (distance <= WALLDISTANCE and eventCounter == 2):
        stop()
        while distance <= WALLDISTANCE:
            distance = distanceSensor.distance_centimeters
            sleep(5)
        eventCounter = 3
        continue

    if (distance <= WALLDISTANCE and eventCounter == 3):
        stop()
        throwBall()
        coursCompleted = True
        continue

    if (left < rightCompare and
            right < leftCompare) and\
            ((left + right) / 2) > (middleCompare):
        forward(SPEED)
        continue
    elif right > leftCompare:
        turnLeft(SPEED, SPEED)
        continue
    elif rightCompare < left:
        turnRight(SPEED, SPEED)
        continue
    else:
        forward(SPEED)
        continue

# Sunaa Risu
