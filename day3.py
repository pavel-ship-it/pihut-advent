# Day 3 of PiHut Codemas 2022
# Pushing the buttons

# Imports
from machine import Pin
import time

# Set up our button names and GPIO pin numbers
# Also set pins as inputs and use pull downs
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

while True: # Loop forever

    time.sleep(0.25) # Short delay
            
    if button1.value() == 1: #If button 1 is pressed
        print("Button 1 pressed")
        green.toggle() # Toggle Red LED on/off
        
    if button2.value() == 1: #If button 2 is pressed
        print("Button 2 pressed")
        amber.toggle() # Toggle Red LED on/off

    if button3.value() == 1: #If button 3 is pressed
        print("Button 3 pressed")
        red.toggle() # Toggle Red LED on/off