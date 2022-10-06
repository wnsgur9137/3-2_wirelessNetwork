from picamera import PiCamera
from time import sleep

#import picamera
# import time
#camera = picamera.Picamera()
# time.sleep(5)

camera = PiCamera()
	
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/3-2_wirelessNetwork/week6/testimage.jpg')
camera.stop_preview()
