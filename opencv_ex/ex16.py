# -*- coding: EUC-KR -*-
# ȭ������ - �÷� ����(BGR)
import cv2
# import numpy as np

img = cv2.imread('./data/lena.jpg')
img[120, 300] = [255, 0, 0] # �÷� (BGR) ����
print(img[100:110, 200:210]) # �Ķ������� ����

img[100:400, 200:300] = [255, 0, 0] # ROI ����

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()