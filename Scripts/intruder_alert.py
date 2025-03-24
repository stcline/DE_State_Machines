# This script will create an alarm system that will alert the user if the following conditions are met:
#   The systme is armed using a button, AND
#   The ultrasonic sensor detects an object within a certain range, OR
#   The sound sensor detects a loud noise, OR
#   The light sensor detects a sudden change in light intensity.
#
# This system runs from a Raspberry Pi 3 Model B+ with the following components:
#   - Ultrasonic sensor (HC-SR04)
#   - Sound sensor (KY-038)
#   - Light sensor (TSL2561)
#   - Button
#   - Buzzer

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

# Set up pins for the sound sensor
SOUND = 17
GPIO.setup(SOUND, GPIO.IN)

# Set up pins for the light sensor
LIGHT = 27
GPIO.setup(LIGHT, GPIO.IN)

# Set up pins for the button
BUTTON = 22
GPIO.setup(BUTTON, GPIO.IN)

# Set up pins for the buzzer
BUZZER = 18
GPIO.setup(BUZZER, GPIO.OUT)

# Set up global variables
armed = False
alarm = False

#TODO - Fix this code in this function
# Function to arm the system using the button
def arm_system():
    global armed
    if BUTTON == 0:
        armed = not armed
        if armed:
            print("System armed")
        else:
            print("System disarmed")

# Function to check the ultrasonic sensor
def check_ultrasonic():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return distance

# Function to check the sound sensor
def check_sound():
    return GPIO.input(SOUND)

# Function to check the light sensor
def check_light():
    return GPIO.input(LIGHT)

# Function to sound the alarm
def sound_alarm():
    GPIO.output(BUZZER, True)
    time.sleep(1)
    GPIO.output(BUZZER, False)
    time.sleep(1)

# Add event detection for the button
# This is a more advance method of detecting button presses.  If you want to teach this, uncomment the code below and omit the code for the while loop which checks if the button is pressed.
# GPIO.add_event_detect(BUTTON, GPIO.FALLING, callback=arm_system, bouncetime=200)

# Main loop
while True:
    # Omit this code if you are using the event detection method for the button
    if GPIO.input(BUTTON) == 0: # Check if the button is pressed
        arm_system(0) # Call the arm_system function
        if armed:
            distance = check_ultrasonic()
            sound = check_sound()
            light = check_light()
            if distance < 100 or sound or light:
                if not alarm:
                    alarm = True
                    sound_alarm()
        else:
            alarm = False
        time.sleep(0.1)

# Clean up GPIO pins
GPIO.cleanup()