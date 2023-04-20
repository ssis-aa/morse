# morse
Send and receive Morse code with the Circuitplayground Express.

## Morse Code Challenge

Mr. Kreier has a board that is sending morse code via a flashing light. The rate at which he is sending Morse code is Here is some information you might want to know:

Morse code consists of a dot (.) and a dash (-). Each letter is a combination of dots and dashes. You can Google to find this out. 

Mr. Kreier is pausing three dots worth of time between letters. After a full word is sent, his code waits seven dots worth of time before sending the word again.

[This REPL has a version of the fan blade analyzer code adapted for this task](https://replit.com/@evanweinberg/Morse-Code-Analyzer-Starter-Code). The only real change to the code is the name change of the input file. The morse_light_raw.csv file contains time and light sensor data for a Circuitpython board that was put next to Mr. Kreier's sending device.

Your challenge is as follows:

- 5 points - figure out the length of time in seconds for a dot and a dash 
- 10 points - threshold the light data into zeros and ones.
- 10 points - write code to automatically measure the length of time in seconds for each light pulse in the data. (This is basically what I asked you to do for the picket fence task)
- 10 points - write code to turn the widths of each pulse into a 1 or a 3 where a 1 represents a dot and a 3 represents a dash.
- 10 points - Turn a series of pulses into a Python list that represents a series of dots and dashes. For example, the list for the letter 'L' is  [1,3,1,1], because the Morse Code for 'L' is dot-dash-dot-dot.
- 15 points - Process the entire morse_light_raw.csv file into a list of lists, each one corresponding with a single letter. For example: [[1,3,1,1],[3,3,3],[1,3,3,1],[1,3,3,1],[1,1,1]] is a list that represents the word 'LOOPS'
- 10 points - use the content of the morse.py to translate each list of pulses into a letter.
- 5 points - translate the morse code message into a word

## Code in Circuitpython

We need 2 use cases: a Circuitplayground Express as sender of the information, and another one as receiver.

``` py
# Sending morse code using neopixels

import neopixel
neo = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05, auto_write=False)

message = "HELLO WORLD"

letters = {"A":[1,3],"B":[3,1,1,1],"C":[3,1,3,1],"D":[3,1,1],"E":[1],"F":[3,1,1,1],"G":[3,3,1],
"H":[1,1,1,1],"I":[1,1],"J":[1,3,3,3],"K":[3,1,3],"L":[1,3,1,1],"M":[3,3],"N":[3,1],"O":[3,3,3],
"P":[1,3,3,1],"Q":[3,3,1,3],"R":[1,3,1],"S":[1,1,1],"T":[3],"U":[1,1,3],"V":[1,1,1,3],
"W":[1,3,3],"X":[3,1,1,3],"Y":[3,1,3,3],"Z":[3,3,1,1]}
```

And the decoder:

``` py
# Receiving and decoding the message
# Probably need some calibration code for pulse width and light intensity average

input = phototransistor.A8
```
