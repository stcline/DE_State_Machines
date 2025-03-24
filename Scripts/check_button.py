# Import necessary libraries
import time
import RPi.GPIO as GPIO

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up pins for the button
BUTTON = 22
GPIO.setup(BUTTON, GPIO.IN)

# Function to check the button
def check_button():
    return GPIO.input(BUTTON)

while True:
    print(check_button())
    time.sleep(1)