import board
import neopixel
import os
import sys
import time
from digitalio import DigitalInOut, Direction, Pull
from parser import *
from config import *

# Internal neopixel
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.01)

# Internal red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Digital input with pullup on D2, D3, and D4
buttons = []
for p in [board.D2, board.D3, board.D4]:
    button = DigitalInOut(p)
    button.direction = Direction.INPUT
    button.pull = Pull.UP
    buttons.append(button)


def open_routine(routine):

    print(f"> {routine} executing", end="\n")
    dot.fill((150, 150, 0))
    dot.show()
    execute_routine(routine)
    print("> Completed.")
    time.sleep(1)


prewait = config()["prewait"]

if prewait:
    print(f"\nWaiting {prewait} second(s).")
    time.sleep(prewait)

print("\n\n-----READY-----\n")

while True:
    dot.fill((0, 255, 0))
    dot.show()

    if config()["automatic"]:
        time.sleep(2)
        open_routine(config()["default_script"])
        sys.exit()

    if not buttons[0].value:
        open_routine("routines/routine_a.osl")

    if not buttons[1].value:
        open_routine("routines/routine_b.osl")

    if not buttons[2].value:
        open_routine("routines/routine_c.osl")

    if config()["clear"]:
        print("")

"""
DO:
* External storage exfiltration
* Neopixel control
* Unix storage exfiltration
* Additional mouse commands args (click)
"""

"""
DONE:
* External payload (EP:)
* OSL to serial (SER:)
* Refactor and separate parser
* JSON config
* Automatic OSL script
* Looping (ind. & set int)
* Empty line error PARTLY DONE, CRLF shit
* Recursive looping / loop within loop
* Variables (VAR:)
"""

"""
DEFER:
* Automatic obfuscation (Missing zlib; EP should be pre-obfuscated anyway)
* OLED screen control
* Wifi enabled control
* Multiline strings (MS:)
* Duckyscript -> OSL
* Joystick support
"""
