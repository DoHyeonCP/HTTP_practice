# -*- coding: EUC-KR -*-
# ȭ�� ����: �׷��� ������ ����
import cv2
# import numpy as np

img = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
img[120,200] = 0 # ȭ�Ұ�(���, �۷��̽�����) ����
print(img[100:110, 200:210]) # ROI ����

# for y in range(100, 400):
#     x in range(200, 300):
#         img[y, x] = 0

img[100:400, 200:300] = 0 # ROI ����

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()