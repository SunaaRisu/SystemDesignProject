#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, MoveTank, Motor

tankDrive = MoveTank(OUTPUT_A, OUTPUT_B)
motor3 = Motor(OUTPUT_C)

def forward(speed):
    tankDrive.on(speed, speed)


def turnLeft(speed, innerWheelBraking):
    tankDrive.on(speed - innerWheelBraking, speed)


def turnRight(speed, innerWheelBraking):
    tankDrive.on(speed, speed - innerWheelBraking)


def turn180():
    tankDrive.on(0, 0)
    tankDrive.on_for_rotations(30, 30, 1)
    tankDrive.on_for_rotations(-30, 30, 1.1)


def stop():
    tankDrive.on(0, 0)


def throwBall():
    motor3.on_for_rotations(30, 0.2)

# Sunaa Risu
