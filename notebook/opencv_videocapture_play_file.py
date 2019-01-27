import cv2
import sys

file_path = 'data/temp/sample_video.mp4'
delay = 1
window_name = 'frame'

cap = cv2.VideoCapture(file_path)

if not cap.isOpened():
    sys.exit()

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow(window_name, frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

cv2.destroyWindow(window_name)
