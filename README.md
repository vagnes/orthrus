# Orthrus

<img src="./img/logo_black.png" alt="Orthrus logo" width="200" />

Orthrus is a HID/keystroke injection device written in CircuitPython, primarily for the Adafruit M4 Airlift Lite.

Scripts are written in OSL (Orthrus Scripting Language) and the following commands are currently available:

| Command                             | Description                                            |
| ----------------------------------- | ------------------------------------------------------ |
| K: \<KEYCODE>                       | Keycode command                                        |
| C: \<CCC>                           | Consumer control code command                          |
| S: \<STRING>                        | HID injects string                                     |
| SL: \<STRING>                       | HID injects string and presses ENTER                   |
| LOOP: \<INT>                        | Demarcates the beginning of the loop and loops n times |
| ELOOP                               | Demarcates the end of the loop                         |
| VAR: \<NAME>, \<VALUE>              | Sets variable                                          |
| \{\{\<VAR NAME>\}\}                 | Use variable                                           |
| OSL: \<PATH \(as string\)>          | Run external OSL fragments within an OSL script        |
| M\[move\]: X\(\<INT>\), Y\(\<INT>\) | Moves the mouse \(X, Y coordinates\)                   |
| M\[click\]                          | Clicks the mouse \(right or left mouse button\)        |
| EP: \<PATH \(as string\)>           | Injects external payload                               |
| SLEEP: \<FLOAT>                     | Sleeps for n seconds until executing next line         |
| SER: \<STRING>                      | Print string to serial console                         |
| QUIT                                | Quits the routine/script                               |

Please see examples in the "routines" folder.

## Installation

Simply clone this repository to your Adafruit Metro M4 Airlift Lite and make sure you have the required libraries installed.

### Required libraries

* Adafruit HID
* Neopixel
* Simpleio

## Running

The software should start automatically.

The current configuration is three buttons (at digital pins 2, 3 and 4) which corresponds to routine_a.osl, routine_b.osl and routine_c.osl respectively.

## Todo and planned features

* OLED screen control
* Wifi enabled control
* Duckyscript -> OSL
* Joystick/gamepad support
* Add counter in OSL
* Neopixel control with OSL

## Acknowledgements

The logo was made by [Johannes T. Røsvik](https://github.com/rosvik/)
