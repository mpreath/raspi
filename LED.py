#!/usr/bin/python

import RPi.GPIO as GPIO
import time
pinNum1 = 11
pinNum2 = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinNum1,GPIO.OUT)
GPIO.setup(pinNum2,GPIO.OUT)


while True:
	GPIO.output(pinNum1, GPIO.HIGH)
	GPIO.output(pinNum2, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(pinNum1, GPIO.LOW)
	GPIO.output(pinNum2, GPIO.HIGH)
	time.sleep(0.5)
