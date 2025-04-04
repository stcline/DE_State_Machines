# This script is designed to run on a Raspberry Pi and uses GPIO pins to interact with various sensors.
# The setup creates a "follow my lead" game where the user has to imitate actions based on random sensor triggers.
# It generates a random number in order to choose which action the user imitates.  Each action is associated with a different sensor.
# User actions are as follows:
# push = push button
# turn = potentiometer
# light = light sensor (Shine light on the sensor to trigger it)
# # motion = PIR motion sensor (put your hand in front of the sensor to trigger it)
# distance = ultrasonic sensor (put an object in front of the sensor to trigger it)

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

# Function to generate a random number between 1 and 5
def generate_random_number():
    return random.randint(1, 5)

#pseudo code for the game:
# while user does not make a mistake
#     get random leader instruction 
#     get user response
#    if user response matches leader instruction
#          indicate match and keep playing
#    otherwise
#         quit

# Main game loop

while True:
    # Generate a random number to determine the action
    action = generate_random_number()
    
    # Print the action for debugging purposes
    print(f"Action: {action}")
    
    # Perform the action based on the random number
    if action == 1:
        print("Push the button!")
        while not check_button():
            time.sleep(0.1)
        print("Button pushed!")
        
    elif action == 2:
        print("Turn the potentiometer!")
        while not check_pot():
            time.sleep(0.1)
        print("Potentiometer turned!")
        
    elif action == 3:
        print("Shine light on the sensor!")
        while not check_light():
            time.sleep(0.1)
        print("Light sensor triggered!")
        
    elif action == 4:
        print("Move in front of the motion sensor!")
        while not check_motion():
            time.sleep(0.1)
        print("Motion sensor triggered!")
        
    elif action == 5:
        print("Put an object in front of the ultrasonic sensor!")
        while check_distance() > 0.2:  # Adjust distance threshold as needed
            time.sleep(0.1)
        print("Ultrasonic sensor triggered!")
        
    else:
        print("Invalid action!")
        # end the script if invalid action is generated
        break

    # Add a small delay to avoid rapid looping
    time.sleep(0.2)
    