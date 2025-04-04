# This script is designed to run on a Raspberry Pi and uses GPIO pins to interact with various sensors.
# It will test the current state of the sensors and print the results to the console.
# The script will run indefinitely until interrupted.

# Import necessary libraries
import time
import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
import random

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up pins for the button
BUTTON = 22
GPIO.setup(BUTTON, GPIO.IN)

# Set up pins for the potentiometer
POT_PIN = 23
GPIO.setup(POT_PIN, GPIO.IN)

# Set up pins for the light sensor
LIGHT = 18
GPIO.setup(LIGHT, GPIO.IN)

# Set up object for the ultrasonic sensor
ultrasonic = DistanceSensor(echo=17, trigger=4)

# Set up pins for the PIR motion sensor
MOTION = 27
GPIO.setup(MOTION, GPIO.IN)

# Function to check the button
def check_button():
    return GPIO.input(BUTTON)

# Function to check the potentiometer
def check_pot():
    return GPIO.input(POT_PIN)

# Function to check the light sensor
def check_light():
    return GPIO.input(LIGHT)

# Function to check the ultrasonic sensor
def check_distance():
	return ultrasonic.distance

# Function to check the motion sensor
def check_motion():
    return GPIO.input(MOTION)

while True:
    # Check the state of each sensor and print the results
    button_state = check_button()
    pot_state = check_pot()
    light_state = check_light()
    distance = check_distance()
    motion_state = check_motion()

    print(f"Button: {button_state}, Potentiometer: {pot_state}, Light: {light_state}, Distance: {distance:.2f} m, Motion: {motion_state}")
    
    # Sleep for a short period before checking again
    time.sleep(0.5)