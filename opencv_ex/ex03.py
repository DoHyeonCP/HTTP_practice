# 비디오 캡처와 화면 출력
import cv2

cap = cv2.VideoCapture(0)  # 0번 카메라
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
							int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size = ', frame_size)

while True:
	retval, frame = cap.read() # 프레임 캡쳐
	if not retval: break

	cv2.imshow('frame', frame)
	key = cv2.waitKey(25)
	if key == 27: break
if cap.isOpened():
	cap.release()

cv2.destroyAllWindows()