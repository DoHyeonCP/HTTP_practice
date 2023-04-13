# -*- coding: EUC-KR -*-
# ���� �Ӽ�
import cv2
import numpy as np

img = cv2.imread('./data/lena.jpg')
#img = cv2.imread('./data/lena/.jpg', cv2.IMREAD_GRAYSCALE)

print('imgs.dmin =', img.ndim)
print('img.shape=', img.shape)
print('mge.dtypa=', img.dtype)

# np.boll, np.uint16, np.unint32, np.float(32, np.float64, np.complex64
img = img.astype(np.int32)
print('img.dtype=', img.dtype)

img = np.uint8(img)
print('img.dtype=', img.dtype)