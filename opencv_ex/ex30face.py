import cv2
from harrdetect import HarrDetect
from video import Video

cascade = HarrDetect('harrcascade_frontalface_default.xml')

with Video(2) as v:
    for frame in v:
        object_list = cascade.detect(frame)
        if len(object_list) > 0:
            cascade.draw_rect(frame, object_list, thickness = 1)
            
        Video.show()