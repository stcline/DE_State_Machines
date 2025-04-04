# This script is designed to work with a Raspberry Pi and an ultrasonic sensor, light sensor and three LEDs.
# It runs like a traffic light system cycling through green, yellow and red under normal circumstances.
# The ultrasonic sensor detects distance, the sound sensor detects sound, and the light sensor detects light intensity.
# It checks for the following conditions:
# - The light around the system dims.
# - Any object approaches the system.
# When, both of those conditions occur the simulation implements an emergency preemption and turns on the red LED.

# Import necessary libraries
import time
import RPi.GPIO as GPIO

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up pins for the ultrasonic sensor
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Set up pins for the light sensor
LIGHT = 27  
GPIO.setup(LIGHT, GPIO.IN)

# Set up pins for the LEDs
GREEN_LED = 17
YELLOW_LED = 22
RED_LED = 18
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(YELLOW_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

# Set up global variables
armed = False
alarm = False
emergency = False

# Function to check the ultrasonic sensor
def check_ultrasonic():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2

    return distance

# Function to check the light sensor
def check_light():
    return GPIO.input(LIGHT)

# Function to control the traffic light system

def traffic_light_system():
    global emergency
    global armed
    global alarm

    while True:
        # Check the light sensor
        light_value = check_light()

        # Check the ultrasonic sensor
        distance = check_ultrasonic()

        # Check for emergency conditions
        if light_value == 0 and distance < 50:
            emergency = True
            print("Emergency detected!")
            GPIO.output(RED_LED, True)
            GPIO.output(GREEN_LED, False)
            GPIO.output(YELLOW_LED, False)
            time.sleep(1)
        else:
            emergency = False
            GPIO.output(RED_LED, False)
            GPIO.output(GREEN_LED, True)
            GPIO.output(YELLOW_LED, False)  
            time.sleep(1)
            GPIO.output(GREEN_LED, False)
            GPIO.output(YELLOW_LED, True)
            time.sleep(1)   
            GPIO.output(YELLOW_LED, False)
            GPIO.output(RED_LED, True)  
            time.sleep(1)

# Main function to run the traffic light system
if __name__ == "__main__":
    try:
        traffic_light_system()
    except KeyboardInterrupt:
        GPIO.cleanup()