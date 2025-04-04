# Import necessary libraries
import time
import RPi.GPIO as GPIO

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up pins for the potentiometer
POT_PIN = 23
GPIO.setup(POT_PIN, GPIO.IN)

# Function to check the potentiometer
def check_pot():
    return GPIO.input(POT_PIN)

while True:
    print(check_pot())
    time.sleep(.2)
