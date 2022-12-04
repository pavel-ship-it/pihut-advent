# Day 4 of PiHut Codemas 2022
# The potential of potentiometer

# Imports (including PWM and ADC)
from machine import ADC, Pin, PWM
import time

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

# Set up the LED pins
red = PWM(Pin(18, Pin.OUT))
amber = PWM(Pin(19, Pin.OUT))
green = PWM(Pin(20, Pin.OUT))


# Set the PWM Frequency
# Sets how often to switch the power between on and off for the LED
red.freq(1000)
amber.freq(1000)
green.freq(1000)

# Create a variable for our reading
reading = 0

while True: # Run forever
    
    reading = potentiometer.read_u16() - 1000 # Read the potentiometer value and set this as our reading variable value
    if reading < 1000:
        reading = 0
    
    print(reading) # Print the reading
    
    # Set the LED PWM duty cycle to the potentiometer reading value
    # The duty cycle tells the LED for how long it should be on each time
    #led.duty_u16(reading)
    if reading <= 20000: # If reading is less than or equal to 20000
        red.duty_u16(reading) # Red ON
        amber.duty_u16(0)
        green.duty_u16(0)
        
    elif 20000 < reading < 40000: # If reading is between 20000 and 40000
        red.duty_u16(reading) 
        amber.duty_u16(reading - 20000) # Amber ON
        green.duty_u16(0)
        
    elif reading >= 40000: # If reading is greater than or equal to 40000
        red.duty_u16(reading) 
        amber.duty_u16(reading)
        green.duty_u16(reading - 40000) # Green ON

    time.sleep(0.0001) # A really short delay
