from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=17, trigger=4)

def check_distance():
	return ultrasonic.distance


while True:
	print(check_distance())
