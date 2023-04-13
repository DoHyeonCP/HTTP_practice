# PIR ��ü�� ĸ���ϱ�
from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

# Create the in-memory stream
stream = BytesIO()

camera = PiCamera()

camera.start_preview()
sleep(2)
camera.capture(stream, format='jpeg')
# ������ �б����� ��Ʈ���� �ǰ�����(rewind)
stream.seek(0)

image = Image.open(stream)
image.show()