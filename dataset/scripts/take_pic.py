import numpy as np
import cv2
import sys
import RPi.GPIO as GPIO
import time
import subprocess


GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

class take_pic():
	def __init__(self, savedir="signalstop",  fname="stop"):
		self.name = fname
		self.savedir = savedir

	def take_pic(self):
		n = self.number_get_write()

		self.pic_LED()
		print(self.savedir)

		cmd = "fswebcam -d /dev/video0 -r 640x480 ./%s%s" % (self.savedir + "/", self.name + str(n) + ".jpg")

		subprocess.call( cmd.strip().split(" ")  )
		print("Save collectly" + self.savedir + "/" + self.name)

	def number_get_write(self):
		f = open('number.txt', 'r')
		
		number = f.read()
		print(number)
		f.close

		f = open('number.txt', 'w')
		num = int(number) + 1
		f.write(str(num))

		f.flush()
		f.close()
		return int(number)

	
	def pic_LED(self):

		for i in range(3):
			GPIO.output(4, GPIO.HIGH)
			time.sleep(0.4)
			GPIO.output(4, GPIO.LOW)
			time.sleep(0.4)


if __name__ == '__main__':
	args = sys.argv
	PIC = take_pic(savedir="beep/test/wrong",fname="wrong")
	if len(args) == 1:
		count = 10
	else:
		count = int(args[1])

	for n in range(count):
		PIC.take_pic()
	GPIO.cleanup()
