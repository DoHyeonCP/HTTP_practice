# -*- coding: EUC-KR -*-
import numpy as np
import cv2

# color ����
blue_color = (255, 0, 0)
gree_color = (0, 255, 0)
red_color = (0, 0, 255)
white_color = (255, 255, 255)

# Font ����
fonts = [
	cv2.FONT_HERSHEY_SIMPLEX,
	cv2.FONT_HERSHEY_PLAIN,
	cv2.FONT_HERSHEY_DUPLEX,
	cv2.FONT_HERSHEY_COMPLEX,
	cv2.FONT_HERSHEY_TRIPLEX,
	cv2.FONT_HERSHEY_COMPLEX_SMALL,
	cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
	cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
	cv2.FONT_ITALIC
]

# ��� 0���� �Ǿ� �ִ� �� Canvas(������)
img = np.zeros((384, 384, 3), np.uint8)

# Font �׸���
for i in range(0, len(fonts)):
	point = 30, 30 + (i *40)
	cv2.putText(img, 'PYTHON', point, fonts[i], 1, white_color, 2, cv2.LINE_AA)

cv2.imshow('text', img)

cv2.waitKey(0)
cv2.destroyAllWindows()