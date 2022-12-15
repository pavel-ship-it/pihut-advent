# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# Fill the strip with turquoise
#strip.fill((72,209,204))
#strip.write()

# Colour variables
red = 255,0,0
green = 0,255,0
blue= 0,0,255

# Define colour list
colours = [red, green, blue]

while True: # Run forever
    # Iterate over the colours
    for j in colours:
        # Then iterate over 15 leds
        for i in range(15):
            strip[i] = (j)
            strip.write()
            time.sleep(0.4)