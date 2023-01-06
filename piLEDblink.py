redLed = 21
greenLed = 20
blueLed = 26
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(redLed, GPIO.OUT)
GPIO.setup(greenLed, GPIO.OUT)
GPIO.setup(blueLed, GPIO.OUT)
while True:
    GPIO.output(redLed, True) 
    #GPIO.output(redLed, GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(redLed, False)
    #GPIO.output(redLed, GPIO.LOW)
    GPIO.output(greenLed, True) 
    #GPIO.output(redLed, GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(greenLed, False)
    #GPIO.output(redLed, GPIO.LOW)
    GPIO.output(blueLed, True) 
    #GPIO.output(redLed, GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(blueLed, False)
    #GPIO.output(redLed, GPIO.LOW)
    #time.sleep(1)
    
