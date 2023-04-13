# -*- coding: EUC-KR -*-
# ���� ���� ���� ��ȭ
# ��ư�� ������ ��ȭ ����
# ��ư�� ���� ��ȭ ����
from gpiozero import Button, MotionSensor
from signal import pause
import cv2
from datetime import datetime

cap = cv2.VideoCapture(0) # 0�� ī�޶�
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
							int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
recorder = None # VideoWriter ��ü
recording_status = False # ��ȭ ������ ���� ���� ����

def start_record():
	global recorder, recording_status
	start = datetime.now()
	fname = start.strftime('/data/%Y%m%d_%H%M%S.mp4')
	recorder = cv2.VideoWriter(fname,fourcc, 20.0, frame_size)
	recording_status = True

def stop_record():
	global recorder, recording_status
	recording_status = False
	if recorder:
		recorder.release()
		recorder = None

button = Button(26)
button.when_pressed = start_record
button.when_released = stop_record

# pir = MotinoSenstor(12)
# pir.when_motion = start record
# pir.when_no_motino = stoprecord

while True:
	retval, frame = cap.read() #������ ĸ��
	if not retval: break

	if recording_status: # ��ȭ���� ��쿡�� ó��
		recorder.write(frame)

	cv2.imshow('frame', frame)
	key = cv2.waitKey(25)
	if key == 27: break # ESC

cap.release()
cv2.destroyAllwindows()