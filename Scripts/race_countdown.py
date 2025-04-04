# This script is designed to control a servo motor for a countdown timer along with three LEDs that act like a starting light for a race.
# The system will move the arm of the servo and light the LEDs in a red, yellow, and green sequence.
# The servo will start at 12 o'clock and move to 3 o'clock over a period of 15 seconds.
# The LEDs will light up in the following sequence: red (at the start), yellow (at 12 seconds), and green (at 15 seconds).
# When the green light turns on the message "GO!" will be printed to the console.
# The script will also include a random delay between 0 and 5 seconds before the countdown starts.

# Import necessary libraries
import time
import RPi.GPIO as GPIO
import random
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up pins for the servo motor
SERVO_PIN = 18
GPIO.setup(SERVO_PIN, GPIO.OUT)
servo = GPIO.PWM(SERVO_PIN, 50)  # Set frequency to 50Hz (20ms period)
servo.start(0)  # Start PWM with 0% duty cycle

# Set up pins for the LEDs
GREEN = 24  # GPIO pin for green LED
YELLOW = 25    # GPIO pin for yellow LED
RED = 5  # GPIO pin for red LED
GPIO.setup(GREEN, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(YELLOW, GPIO.OUT, initial=GPIO.LOW)   
GPIO.setup(RED, GPIO.OUT, initial=GPIO.LOW)   

# Function to move the servo arm from 0 to 90 degrees over a period of time
def move_servo(start_angle, end_angle, duration):
    # Calculate the step size
    step_size = (end_angle - start_angle) / (duration * 10)  # 10 steps per second
    current_angle = start_angle

    for _ in range(int(duration * 10)):
        current_angle += step_size
        servo.ChangeDutyCycle(2.5 + (current_angle / 18))  # Convert angle to duty cycle
        time.sleep(0.1)  # Sleep for 0.1 seconds

# Race start sequence
# Turn on the red LED
GPIO.output(RED, GPIO.HIGH)  # Turn on red LED
# Wait for a random delay between 0 and 5 seconds
delay = random.randint(0, 5)
# Start moving the servo arn for 12 seconds
move_servo(0, 72, 12)
GPIO.output(RED, GPIO.LOW)  # Turn off red LED
GPIO.output(YELLOW, GPIO.HIGH)  # Turn on yellow LED
# Move the servo arm for 3 seconds
move_servo(72, 90, 3)
GPIO.output(YELLOW, GPIO.LOW)  # Turn off yellow LED
GPIO.output(GREEN, GPIO.HIGH)  # Turn on green LED
print("GO!")  # Print "GO!" to the console    