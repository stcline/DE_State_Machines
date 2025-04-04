# Import necessary libraries
import time
import RPi.GPIO as GPIO

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up pins for the PIR motion sensor
MOTION = 27
GPIO.setup(MOTION, GPIO.IN)

# Function to check the motion sensor
def check_motion():
    return GPIO.input(MOTION)

while True:
    print(check_motion())
    time.sleep(.2)
