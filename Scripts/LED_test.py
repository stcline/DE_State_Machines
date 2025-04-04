import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

GREEN = 24  # GPIO pin for green LED
YELLOW = 25    # GPIO pin for yellow LED
RED = 5  # GPIO pin for red LED

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BCM)   # Use physical pin numbering
GPIO.setup(GREEN, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(YELLOW, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(RED, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)

while True: # Run forever
    GPIO.output(GREEN, GPIO.HIGH) # Turn on
    sleep(1)                  # Sleep for 1 second
    GPIO.output(GREEN, GPIO.LOW)  # Turn off
    GPIO.output(YELLOW, GPIO.HIGH) # Turn on green LED
    sleep(1)                  # Sleep for 1 second
    GPIO.output(YELLOW, GPIO.LOW)  # Turn off
    GPIO.output(RED, GPIO.HIGH) # Turn on green LED
    sleep(1)                  # Sleep for 1 second
    GPIO.output(RED, GPIO.LOW)  # Turn off