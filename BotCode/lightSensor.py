#!/usr/bin/env python3
from BotCode.MenuLib.menu import calibrationScreen, beep, clear

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import LightSensor

leftSensor = LightSensor(INPUT_1)
middleSensor = LightSensor(INPUT_2)
rightSensor = LightSensor(INPUT_3)


def initialCalibration():
    lsWhite = 100   # ls are values for the Light Sensors
    lsBlack = 0
    csWhite = 100   # cs are values for the Color Sensors
    csBlack = 0
    lsAlpha = 0.5   # value for calculating Black-White-Threshold of the Light Sensors
    csAlpha = 0.3   # value for calculating Black-White-Threshold of the Color Sensor

    action = calibrationScreen()
    if action == 1:
        clear()
        print('White')
        input()
        # Calibrate for White
        # Light Sensors
        lsWhite = 0.5 * (leftSensor.reflected_light_intensity + rightSensor.reflected_light_intensity)
        # Color Sensor
        csWhite = middleSensor.reflected_light_intensity
        beep()
        clear()
        print('Black')
        input()
        # Calibrate for Black
        # Light Sensors
        lsBlack = 0.5 * (leftSensor.reflected_light_intensity + rightSensor.reflected_light_intensity)
        # Color Sensor
        csBlack = middleSensor.reflected_light_intensity
        beep()
        clear()
        print('Normal')
        # calculate threshold
        lsThreshold = lsAlpha * (lsWhite + lsBlack)
        csThreshold = csAlpha * (csWhite - csBlack)
        input()
        # Checking for a normal driving position
        # Light Sensor
        if leftSensor.reflected_light_intensity < lsThreshold or rightSensor.reflected_light_intensity < lsThreshold:
            return 'error'
        if middleSensor.reflected_light_intensity > csThreshold:
            return 'error'
        beep()
        clear()
        print("lsWhite:", lsWhite)
        print("lsBlack:", lsBlack)
        print("lsThreshold:", lsThreshold)
        print("csWhite:", csWhite)
        print("csBlack:", csBlack)
        print("csThreshold:", csThreshold)
        print("Left:", leftSensor.reflected_light_intensity)
        print("Middle:", middleSensor.reflected_light_intensity)
        print("Right:", rightSensor.reflected_light_intensity)
        return lsThreshold, csThreshold
    elif action == 2:
        recalibrate()
    else:
        return 'error'


def recalibrate():
    white = 0.5 * (leftSensor.reflected_light_intensity + rightSensor.reflected_light_intensity)
    black = middleSensor.reflected_light_intensity
    threshold = 0.5 * (white + black)
    return threshold
