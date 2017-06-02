#!/usr/bin/python3
# Filename: maxSonarTTY.py
 
# Reads serial data from Maxbotix ultrasonic rangefinders
# Gracefully handles most common serial data glitches
# Use as an importable module with "import MaxSonarTTY"
# Returns an integer value representing distance to target in millimeters
 
from time import time
from time import sleep
from serial import Serial
 
serialDevice = "/dev/ttyAMA0" # default for RaspberryPi
maxwait = 0.3 # seconds to try for a good reading before quitting
ser = Serial(serialDevice, 9600, 8, 'N', 1, timeout=1)
 
def measure():
 
    timeStart = time()
    valueCount = 0
 
    while time() < timeStart + maxwait:
        if ser.inWaiting():
            bytesToRead = ser.inWaiting()
            valueCount += 1
            if valueCount < 2: # 1st reading may be partial number; throw it out
                continue
            testData = ser.read(bytesToRead)
            if not testData.startswith(b'R'):
                # data received did not start with R
                continue
            try:
                sensorData = testData.decode('utf-8').lstrip('R')
            except UnicodeDecodeError:
                # data received could not be decoded properly
                continue
            try:
                mm = int(sensorData)
            except ValueError:
                # value is not a number
                continue
            ser.close()
            return(mm)
 
    ser.close()
    raise RuntimeError("Expected serial data not received")
 
if __name__ == '__main__':
    while True:
 
        measurement = measure()
        print("distance =",measurement)
        sleep(1)
