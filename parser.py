import usb_hid
import re
import time
import sys
from config import *

from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.mouse import Mouse
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard

# Init HIDs
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
cc = ConsumerControl(usb_hid.devices)
m = Mouse(usb_hid.devices)


def sanitise(line, cmd, remove_space=False):
    line = line.replace(cmd, "")
    if remove_space == True:
        line = line.strip()
    return line


def argument(line):
    x = re.search(r"\[(.*?)\]", line.lower())
    return x.group(1)


def ext_payload(payload):
    pl_file = open(payload, "r")

    for line in pl_file:
        layout.write(line)


def comment_or_empty(line):

    if (line == ""
                    or line.startswith("\n")
                    or line.startswith("\r\n")
                    or line.startswith("//")
            ):
        return True


def is_var(line):
    if line.startswith("VAR", 0):
        line = sanitise(line, "VAR: ")
        return True


def parser(line):

    time.sleep(0.1)

    kk = "Keycode."
    ccc = "ConsumerControlCode."

    # Keycode command
    if line.startswith("K:", 0):
        line = sanitise(line, "K: ", True)
        split_line = line.split(",")
        kk_line = []

        for i in split_line:
            kk_line.append(eval(kk + i.upper()))

        kbd.press(*kk_line)
        kbd.release_all()

    # Sleep/delay command
    elif line.startswith("SLEEP: ", 0):
        time.sleep(float(sanitise(line, "SLEEP: ")))

    # Consumer control code command
    elif line.startswith("C:", 0):
        code = sanitise(line, "C: ", True)
        cc.send(eval(ccc + code))

    # String command
    elif line.startswith("S:", 0):
        line = sanitise(line, "S: ")

        # TODO: FIX CRLF ERROR
        layout.write(line)

    # Send line command
    elif line.startswith("SL:", 0):
        line = sanitise(line, "SL: ")

        # TODO: FIX CRLF ERROR
        layout.write(line)
        kbd.press(eval(kk + "ENTER"))
        kbd.release_all()

    # Mouse movements: MUST have an argument
    elif line.startswith("M", 0):
        arg = argument(line)

        if arg == "move":
            cord = re.search(r"X\((.*?)\).*?Y\((.*?)\)", line.upper())
            cord = [int(float(cord.group(1))), int(float(cord.group(2)))]
            m.move(*cord)

        if arg == "click":  # TODO: Test
            line = sanitise(line, "M[click]:", True)
            if line.lower() == "left":
                m.click(Mouse.LEFT_BUTTON)
            elif line.lower() == "right":
                m.click(Mouse.RIGHT_BUTTON)

    # Inject external payload
    elif line.startswith("EP:", 0):
        payload = sanitise(line, "EP: ")
        ext_payload(payload)

    # Print to serial
    elif line.startswith("SER:", 0):
        line = sanitise(line, "SER: ")
        print(line)

    # End routine execution
    elif line.startswith("QUIT", 0):
        sys.exit()


def is_loop(line):
    return line.startswith('LOOP')


def is_loop_end(line):
    return line.startswith('ELOOP')


def run_code(line):
    parser(line)


def code_runner(current_code):
    if not current_code:
        return  # if not empty
    for i, line in enumerate(current_code):
        if config()["logging"]:
            print(f"{i} | {line}")
        if is_loop(line):
            count = sanitise(line, "LOOP:", True)
            try:
                arg = argument(line)
                if arg == "inf":
                    while(True):
                        code_runner(current_code[i+1:])
            except AttributeError:
                pass  # no argument, hence no inf loop

            rest = None
            for _ in range(int(count)):
                rest = code_runner(current_code[i+1:])
            code_runner(rest)
            break
        if is_loop_end(line):
            return current_code[i+1:]
        run_code(line)


class Executor:

    def __init__(self, command_file):
        self.command_file = command_file

        self.var_container = {}
        self.prevar_commands = []
        self.commands = []

    def create_var(self, line):
        line = re.search(r"VAR:\s(.*?)\,(.*?)$", line.upper())
        self.var_container.update(
            {line.group(1).strip(): line.group(2).strip()})

    def substitute_var(self):

        for line in self.prevar_commands:
            for var in self.var_container:
                line = line.replace("{{%s}}" %
                                    var.upper(), self.var_container[var])
                line = line.replace("{{%s}}" %
                                    var.lower(), self.var_container[var])
            self.commands.append(line)

    def execute_routine(self):

        with open(self.command_file, "r") as f:
            for line in f:
                line = line.strip()
                if comment_or_empty(line):
                    continue
                elif is_var(line):
                    self.create_var(line)
                # Call OSL within OSL scripts
                elif line.startswith("OSL:", 0):
                    line = sanitise(line, "OSL: ")
                    print(line)
                    Executor(line).execute_routine()
                else:
                    self.prevar_commands.append(line)
                print(line)

        # Substitute vars
        self.substitute_var()

        code_runner(self.commands)
