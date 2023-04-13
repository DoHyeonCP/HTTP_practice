from time import sleep
from picamera import PiCamera
from datetime import datetime, timedelta

camera = PiCamera()
camera.start_preview()

for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
	print('Captured %s' % filename)
	sleep(10)