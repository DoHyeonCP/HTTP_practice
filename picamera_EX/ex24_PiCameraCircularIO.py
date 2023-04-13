import io
import random
from picamera import PiCamera, PiCameraCircularIO

def motion_detected():
	# Randomly return True(like a fake motion detection routine)
	return random.randint(0, 10) == 0

camera = PiCamera()
stream = PiCameraCircularIO(camera, seconds = 20)

camerea.start_recording(stream, format = 'h264')
try:
	while True:
		camera.wait_recording(1)
		if motion_detected:
			# ������ ������ٸ� 10�ʰ� ��ȭ�Ͽ� ��ũ�� ��Ʈ���� ���
			camera.wait_recording(10)
			stream.copy_to('motion.h264') # ��Ʈ���� ���Ϸ� �����ϱ�
finally:
	camera.stop_recording()