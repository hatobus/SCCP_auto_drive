import time
import RPi.GPIO as GPIO
import csv

GPIO.setmode(GPIO.BCM)

dlist1 = []
dlist2 = []
dlist3 = []

f = open('distdata.csv', 'ab')
csvWriter = csv.writer(f)

def measure(gp):
    GPIO_TRIGECHO = gp 
    GPIO.setup(GPIO_TRIGECHO,GPIO.OUT)
    GPIO.output(GPIO_TRIGECHO, False)
  # This function measures a distance
  # Pulse the trigger/echo line to initiate a measurement
    GPIO.output(GPIO_TRIGECHO, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGECHO, False)
  #ensure start time is set in case of very quick return
    start = time.time()

  # set line to input to check for start of echo response
    GPIO.setup(GPIO_TRIGECHO, GPIO.IN)
    while GPIO.input(GPIO_TRIGECHO)==0:
        start = time.time()

  # Wait for end of echo response
    while GPIO.input(GPIO_TRIGECHO)==1:
        stop = time.time()
  
    GPIO.setup(GPIO_TRIGECHO, GPIO.OUT)
    GPIO.output(GPIO_TRIGECHO, False)

    elapsed = stop-start
    distance = (elapsed * 34300)/2.0
    time.sleep(0.1)
    return distance

try:

    while True:

        dlist1.append(measure(19))
        dlist2.append(measure(6))
        dlist3.append(measure(26))
        #print "  Distance1 : %.1f cm Distance2 : %.1f cm Distance3 : %.1f cm" % (distance,distance2,distance3)
        time.sleep(1)

except KeyboardInterrupt:
    csvWriter.writerow(dlist1) 
    writer = csv.writer(f, lineterminator='\n')
    csvWriter.writerow(dlist2)
    writer = csv.writer(f, lineterminator='\n')
    csvWriter.writerow(dlist3)
    GPIO.cleanup()
    f.close()