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

# Sunaa Risu
