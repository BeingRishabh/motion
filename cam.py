import RPi.GPIO as GPIO
import time 
import os
GPIO.setmode(GPIO.BCM)
pirPin=6
GPIO.setup(pirPin,GPIO.IN)
def cam1():
    os.system("fswebcam -F 4 --fps 20 -r 800*600 /home/pi/prurish/2.jpg")
    print("pic taken")
while True:
    if GPIO.input(pirPin):
        print("Motion Detected")
        cam1()
        time.sleep(1)
    else:
        print("nothing detected")
