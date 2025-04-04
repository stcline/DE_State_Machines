# Import necessary libraries
import time
import RPi.GPIO as GPIO

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up pins for the sound sensor
SOUND = 27
GPIO.setup(SOUND, GPIO.IN)

# Function to check the sound sensor
def check_sound():
    return GPIO.input(SOUND)

while True:
    print(check_sound())
    time.sleep(.2)
