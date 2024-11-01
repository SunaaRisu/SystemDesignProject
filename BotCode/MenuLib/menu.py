#!/usr/bin/env python3

from time import sleep
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.console import Console

btn = Button()
sound = Sound()
screen = Console()

screen.set_font(font='Lat15-Terminus12x6.psf.gz', reset_console=True)


def clear():
    screen.reset_console()


def beep():
    sound.beep()


def calibrationScreen():
    print('Full Calibration (Button Up)\nFast Calibration (Button Down)')
    while True:
        if btn.up:
            sound.beep()
            screen.reset_console()
            print('After Beep place all Sensors on\nWhite and press Enter.\nWait for Beep.\nDo the same for all\nSensors on Black and\nnormal driving position.\nPress Enter to start...')
            input()
            sound.beep()
            return 1
        if btn.down:
            sound.beep()
            screen.reset_console()
            print('Place Bot on the Line.\nLeft and Right Sensor\non White, Middle Sensor on Black.\nPress Enter to continue...')
            input()
            return 2
