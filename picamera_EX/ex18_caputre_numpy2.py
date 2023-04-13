import time
from picamera import PiCamera
import numpy as np
import cv2

with PiCamera() as camera:
	camera.resolution = (640, 480)

	image = np.empty((480, 640, 3), dtype=np.uint8)

	while True:
		camera.capture(image, 'bgr')
		cv2.imshow('frame', image)
		if cv2.waitKey(1) == 27: # esc 키 입력시 종료
			break