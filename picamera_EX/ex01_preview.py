from picamera import PiCamera
from time import sleep

camera = PiCamera()

# 180�� ȸ���ϱ�
# camera.rotation = 180

camera.start_preview() # �̸����� ȭ�� ����
#camera.start_preview(alpha = 200) # ���۵� ����, ���� ���� : 0 ~ 255

sleep(10)

camera.stop_preview() # �̸����� ȭ�� ����