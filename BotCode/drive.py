#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank

tankDrive = MoveTank(OUTPUT_A, OUTPUT_B)


def forward(speed):
    tankDrive.on(speed, speed)


def turnLeft(speed, innerWheelBraking):
    tankDrive.on(speed - innerWheelBraking, speed)


def turnRight(speed, innerWheelBraking):
    tankDrive.on(speed, speed - innerWheelBraking)


def turn180():
    tankDrive.on(0, 0)
    tankDrive.on_for_rotations(-50, 0, 1.2)
    tankDrive.on_for_rotations(0, 50, 1.2)


def turn180OnSpot():
    tankDrive.on(0, 0)
    tankDrive.on_for_rotations(50, 50, 1)
    tankDrive.on_for_rotations(-50, 50, 1.2)


def stop():
    tankDrive.on(0, 0)

# Sunaa Risu
