#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank

tankDrive = MoveTank(OUTPUT_A, OUTPUT_B)


def forward(speed):
    tankDrive.on(speed, speed)


def turnLeft(speed, innerWheelBraking):
    tankDrive(speed - innerWheelBraking, speed)


def turnRight(speed, innerWheelBraking):
    tankDrive(speed, speed - innerWheelBraking)


def stop():
    tankDrive(0, 0)
