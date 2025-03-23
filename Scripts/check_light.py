# Import necessary libraries
import time
import RPi.GPIO as GPIO

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up pins for the light sensor
LIGHT = 27
GPIO.setup(LIGHT, GPIO.IN)

# Function to check the light sensor
def check_light():
    return GPIO.input(LIGHT)

while True:
    print(check_light())
    time.sleep (1)
    