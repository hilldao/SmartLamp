#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

LightSensorPin = 29    # pin15
LedPin = 15    # pin15
MotoPin = 37
SWITHCH = 1


def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
	GPIO.setup(LightSensorPin, GPIO.IN)   # Set pin mode as input
	GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
	GPIO.setup(MotoPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the led
	GPIO.output(MotoPin, GPIO.LOW) # Set pin to high(+3.3V) to off the Moto
	

	
def loop():
	while True:	    
		SWITHCH=GPIO.input(LightSensorPin)
		print SWITHCH		
		if SWITHCH :
			print '...led on'
			GPIO.output(LedPin, GPIO.LOW)  # led on
			GPIO.output(MotoPin, GPIO.HIGH)
			p = GPIO.PWM(MotoPin, 400)
			p.start(0)
			p.stop()			
			time.sleep(2)
			print 'led off...'
			GPIO.output(LedPin, GPIO.HIGH) # led off
			GPIO.output(MotoPin, GPIO.LOW)
			time.sleep(2)
		else:
			print 'led off...'
			GPIO.output(LedPin, GPIO.HIGH) # led off
		
def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.output(MotoPin, GPIO.LOW) # Set pin to high(+3.3V) to off the Moto
	GPIO.cleanup()                     # Release resource
	print(" - I have run the cleanup function -")

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
