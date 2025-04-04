# Import necessary libraries
import time
import RPi.GPIO as GPIO

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up pins for the servo motor
SERVO_PIN = 18
GPIO.setup(SERVO_PIN, GPIO.OUT)
servo = GPIO.PWM(SERVO_PIN, 50)  # Set frequency to 50Hz (20ms period)
servo.start(0)  # Start PWM with 0% duty cycle

