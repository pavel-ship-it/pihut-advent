# Imports
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import time

# Set up I2C and the pins we're using for it
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

# Short delay to stop I2C falling over
time.sleep(1)

# Define the display and size (128x32)
display = SSD1306_I2C(128, 32, i2c)

while True:
    
    # Delay
    time.sleep(0.5)
        
    # Clear the display
    display.fill(0)
    
    # Write two lines to the display
    # The line turns our light variable into a string, and adds '%' to the end
    display.text("Hello frens",10,14)

    # Update the display
    display.show()