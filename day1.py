#     Day 1 of PiHut Codemas 2022
# Mostly about setting up the environment
# Install and configure Thonny.app
# Connect and run Raspi with the "Hello world" below

from machine import Pin
onboardLED = Pin(25, Pin.OUT)
onboardLED.value(0)

print("This is my Pico talking")