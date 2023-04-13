# picamera ���̺귯�� ����Ʈ
import picamera

# time ���̺귯�� ����Ʈ

# PiCamera ��ü �ν��Ͻ� ����
with picamera.PiCamera() as camera:

	# �ػ󵵸� �����ϵ��� ��
	res = int(input('Resoulution(1:320x240, 2:640x480, 3:1024x768)'))

	# ������ ���� ���� �ػ� ����
	if res == 3:
		camera.resolution = (1024,768)
	elif res == 2:
		camera.resolution = (640, 480)
	else:
		camera.resolution = (320, 240)
	
	# ���ϸ� �Է� �ޱ�
	filename = input('File Name?')

	# ������ ȭ�� ǥ��
	camera.start_preview()

	# 1�� ���
	time.sleep(1)

	# ������ ����
	camera.stop_preview()

	# �Կ��ϰ� ����
	camera.capture(filename + '.jpg')