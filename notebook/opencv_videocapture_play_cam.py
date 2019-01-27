import cv2
import sys

camera_id = 0
delay = 1
window_name = 'frame'

cap = cv2.VideoCapture(camera_id)

if not cap.isOpened():
    sys.exit()

while True:
    ret, frame = cap.read()
    cv2.imshow(window_name, frame)
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)
