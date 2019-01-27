import cv2

cap_cam = cv2.VideoCapture(0)
print(type(cap_cam))
# <class 'cv2.VideoCapture'>

print(cap_cam.isOpened())
# True

cap_cam_wrong = cv2.VideoCapture(1)
print(type(cap_cam_wrong))
# <class 'cv2.VideoCapture'>

print(cap_cam_wrong.isOpened())
# False

cap_cam.release()
