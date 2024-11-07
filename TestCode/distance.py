#!/usr/bin/env python3

from ev3dev2.sensor.lego import UltrasonicSensor

distanceSensor = UltrasonicSensor()

while True:
    print(distanceSensor.distance_centimeters, 'cm')
