# -*- coding: EUC-KR -*-
#ȭ������ - �÷�����(ä�� ����)
import cv2
# import numpy as my
img = cv2.imread('./data/lena.jpg')

# for y in range(100, 400):
#		 x in range(200, 300):
#				 img[y, x, 0] = 255 # B-ä���� 255�� ����

img[100:400, 200:300, 0] = 255 # B-ä���� 255�� ����
img[100:400, 200:300, 1] = 255 # G-ä���� 255�� ����
img[100:400, 200:300, 2] = 255 # R-ä���� 255�� ����

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()