# -*- coding: EUC-KR -*-
# 화소접근 - 컬러 영상(BGR)
import cv2
# import numpy as np

img = cv2.imread('./data/lena.jpg')
img[120, 300] = [255, 0, 0] # 컬러 (BGR) 변경
print(img[100:110, 200:210]) # 파란색으로 변경

img[100:400, 200:300] = [255, 0, 0] # ROI 접근

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()