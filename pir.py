import RPi.GPIO as GPIO
import time, sys
import os
from pushbullet import PushBullet
from picamera import PiCamera
import datetime
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(21,GPIO.IN)
led_red = 2
led_green = 3
GPIO.setup(led_red,GPIO.OUT)
GPIO.setup(led_green,GPIO.OUT)
camera = PiCamera()
apiKey="your key"
p = PushBullet(apiKey)
devices = p.get_device('your devices')
def getFileName():
	return '/home/pi/program/picture/' + datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S') + '.png'
while True:  
    input_state = GPIO.input(21)
    if input_state == True:
        GPIO.output(10,1)
        GPIO.output(led_green,0)
        GPIO.output(led_red,1)
        print('Motion Detected')        
        push = devices.push_note("Alert!!","Intruder Alert!")
        timeCaptured = getFileName()
        camera.rotation = -90
        camera.capture(timeCaptured)
        print("Image Captured")
        print("Uploading...")
        GPIO.output(10,0)
        with open(timeCaptured, "rb") as pic:
            file_data = p.upload_file(pic, "alert.jpg")
        push = p.push_file(**file_data)
    else :
        print('SAFE!')
        GPIO.output(10,0)
        GPIO.output(led_red,0)
        GPIO.output(led_green,1)
        time.sleep(2)
