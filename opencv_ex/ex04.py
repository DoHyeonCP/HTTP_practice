import cv2

cap = cv2.VideoCapture('http://192.168.0.2:4747/video') # droid cam

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
							int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size = ', frame_size)

while True:
	retval, frame = cap.read() # ÇÁ·¹ÀÓ Ä¸Ã³
	if not retval: break

	cv2.imshow('frame', frame)
	key = cv2.waitKey(25)
	if key == 27 : break

if cap.isOpend():
	cap.releas()

cv2.destroyAllWindows()