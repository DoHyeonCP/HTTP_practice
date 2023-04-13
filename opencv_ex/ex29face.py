# -*- coding: EUC-KR -*-
import cv2
import cv2
from cv2.data import haarcascades
from os import path
from video import Video

face_xml = path.join(haarcascades, 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(face_xml)

FACE_WIDTH = 200

def detect_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        minLength = min(w,h)
        if minLength < 150: break # 너무 작은 영역은 무시

        width = max(w,h)
        # 얼굴 부분 검출 (정사각형으로 영역 지정)
        x = x + w//2 - width //2
        y = y + h//2 - width//2
        face_image = frame[y:y+width, x:x+width].copy()

        # 얼굴 영역 표시
        cv2.rectangle(frame,(x,y),(x+width,y+width),(255,0,0),20)
        # 얼굴 부분만 좌즉 상단에 출력
        face_image = cv2.resize(face_image, dsize = (FACE_WIDTH, FACE_WIDTH),
                                                        interpolation=cv2.INTER_AREA)
        frame[0:FACE_WIDTH, 0,:FACE_WIDTH] = face_image[:]

with Video(0) as v:
	for image in v:
		image = detect_face(image)
		# 보여주기
		if not Video.show(image): break

cv2.destroyAllWindows()