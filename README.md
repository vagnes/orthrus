# Orthrus

<img src="./img/logo_black.png" alt="Orthrus logo" width="200" />

Orthrus is a HID/keystroke injection device written in CircuitPython, primarily for the Adafruit M4 Airlift Lite.

Scripts are written in OSL (Orthrus Scripting Language) and the following commands are currently available:

| Command                                  | Description                                            |
| ---------------------------------------- | ------------------------------------------------------ |
| K: \<KEYCODE>                            | Keycode command                                        |
| C: \<CCC>                                | Consumer control code command                          |
| S: \<STRING>                             | HID injects string                                     |
| SL: \<STRING>                            | HID injects string and presses ENTER                   |
| LOOP: \<INT>                             | Demarcates the beginning of the loop and loops n times |
| ELOOP                                    | Demarcates the end of the loop                         |
| VAR: \<NAME>, \<VALUE>                   | Sets variable                                          |
| \{\{\<VAR NAME>\}\}                      | Use variable                                           |
| OSL: \<PATH \(as string\)>               | Run external OSL fragments within an OSL script        |
| M\[move\]: X\(\<INT>\), Y\(\<INT>\)      | Moves the mouse \(X, Y coordinates\)                   |
| M\[click\]: \<left> or \<right>          | Clicks the mouse \(right or left mouse button\)        |
| G\[press\]: \<INT>                       | Press and release a gamepad button (1-16)              |
| G\[hold\]: \<INT>                        | Press and hold a gamepad button (1-16)                 |
| G\[release\]: \<INT>                     | Release a gamepad button (1-16)                        |
| G\[release_all\]                         | Press all gamepad buttons                              |
| G\[center\]                              | Centre all joysticks                                   |
| G\[joy_left\]: X\(\<INT>\), Y\(\<INT>\)  | Move left joystick to absolute position (+/- 127)      |
| G\[joy_right\]: X\(\<INT>\), Y\(\<INT>\) | Move left joystick to absolute position (+/- 127)      |
| G\[reset\]                               | Reset the gamepad state                                |
| EP: \<PATH \(as string\)>                | Injects external payload                               |
| SLEEP: \<FLOAT>                          | Sleeps for n seconds until executing next line         |
| SER: \<STRING>                           | Print string to serial console                         |
| QUIT                                     | Quits the routine/script                               |

Please see examples in the "routines" folder.

## Gamepad example buttons scheme (Xbox One)

ABXY: 1,2,3,4

LSB, RSB, LT(float), RT(float): 5,6,7,8

BACK, START: 9,10

LSC, RSC: 11,12

D-Pad, NSEW: 13,14,15,16

## Installation

Simply clone this repository to your Adafruit Metro M4 Airlift Lite and make sure you have the required libraries installed.

### Required libraries

- Adafruit HID
- Neopixel
- Simpleio

## Running

The software should start automatically.

The current configuration is three buttons (at digital pins 2, 3 and 4) which corresponds to routine_a.osl, routine_b.osl and routine_c.osl respectively. In the `config.py` file, you can set `"automatic": true,` which will run the `automatic.osl` script after a few seconds.

## Todo and planned features

- Duckyscript -> OSL
- Add counter in OSL
- Neopixel control with OSL
- OLED screen control
- Wifi enabled control

## Acknowledgements

The logo was made by [Johannes T. Røsvik](https://github.com/rosvik/)
