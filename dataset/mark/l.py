import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.OUT)

for i in range(5):
	GPIO.output(4, True)
	time.sleep(1)
	GPIO.output(4, False)
	time.sleep(1)

GPIO.cleanup()
