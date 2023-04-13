# -*- coding: EUC-KR -*-
# ���� ������ ��ȯ(Ȯ��/���, ȸ��)
import cv2
import numpy as np

src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)

# rows, cols, channels = src.shape
rows, cols = src.shape
M1 = cv2.getRotationMatrix2D((rows/2, cols/2), 45, 0.5) # �߽���ǥ, ȸ����, ����
M2 = cv2.getRotationMatrix2D((rows/2, cols/2), -45, 1.0)

dist1 = cv2.warpAffine(src, M1, (rows,cols))
dist2 = cv2.warpAffine(src, M2, (rows,cols))

cv2.imshow('dist1', dist1)
cv2.imshow('dist2', dist2)

cv2.waitKey()
cv2.destroyWindows()