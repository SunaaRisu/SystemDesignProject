#!/usr/bin/env python3

from BotCode.MenuLib.menu import beep

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import LightSensor

leftSensor = LightSensor(INPUT_1)
middleSensor = LightSensor(INPUT_2)
rightSensor = LightSensor(INPUT_3)


def calibration():
    white = 0.5 * (leftSensor.reflected_light_intensity + rightSensor.reflected_light_intensity)
    black = middleSensor.reflected_light_intensity
    alpha = 0.5
    threshold = alpha * (white + black)
    if leftSensor.reflected_light_intensity < threshold or middleSensor.reflected_light_intensity > threshold or rightSensor.reflected_light_intensity < threshold:
        return 'error'
    print('white:', white)
    print('black:', black)
    print('threshold:', threshold)
    print("Left:", leftSensor.reflected_light_intensity)
    print("Middle:", middleSensor.reflected_light_intensity)
    print("Right:", rightSensor.reflected_light_intensity)
    beep()
    return threshold

# Sunaa Risu
