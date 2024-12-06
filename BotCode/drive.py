#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank

tankDrive = MoveTank(OUTPUT_A, OUTPUT_B)


def forward(speed):
    tankDrive.on(speed, speed)
    # tankDrive.on_for_rotations(speed, speed, 0.05)


def turnLeft(speed, innerWheelBraking):
    tankDrive.on(speed - innerWheelBraking, speed)
    # tankDrive.on_for_rotations(speed - innerWheelBraking, speed, 0.05)


def turnRight(speed, innerWheelBraking):
    tankDrive.on(speed, speed - innerWheelBraking)
    # tankDrive.on_for_rotations(speed, speed - innerWheelBraking, 0.05)


def turn180():
    tankDrive.on(0, 0)
    tankDrive.on_for_rotations(30, 30, 1)
    tankDrive.on_for_rotations(-30, 30, 1.1)


def stop():
    tankDrive.on(0, 0)

# Sunaa Risu
