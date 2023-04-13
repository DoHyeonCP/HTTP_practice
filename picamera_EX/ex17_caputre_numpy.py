#open cv °´Ã¤·Î Ä¸Ã³ÇÏ±â
import time 
from picamera import PiCamera
import numpy as np
import cv2

with PiCamera() as camera:
	camera.resolution = (640, 480)

	image = np.empty((480, 640, 3), dtype = np.uint8)
	camera.capture(image, 'bgr')
	cv2.imshow('frame', image)
	cv2.waitKey(0)