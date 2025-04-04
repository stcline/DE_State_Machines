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

while True:
    # Move servo to 0 degrees
    servo.ChangeDutyCycle(2.5)  # 0 degrees
    time.sleep(1)  # Wait for 1 second

    # Move servo to 90 degrees
    servo.ChangeDutyCycle(7.5)  # 90 degrees
    time.sleep(1)  # Wait for 1 second

    # Move servo to 180 degrees
    servo.ChangeDutyCycle(12.5)  # 180 degrees
    time.sleep(1)  # Wait for 1 second

