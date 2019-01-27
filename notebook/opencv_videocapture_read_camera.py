import cv2

cap_cam = cv2.VideoCapture(0)
print(type(cap_cam))
# <class 'cv2.VideoCapture'>

print(cap_cam.isOpened())
# True

print(cap_cam.get(cv2.CAP_PROP_POS_FRAMES))
# 0.0

ret, frame = cap_cam.read()

print(ret)
# True

print(type(frame))
# <class 'numpy.ndarray'>

print(frame.shape)
# (720, 1280, 3)

print(cap_cam.get(cv2.CAP_PROP_POS_FRAMES))
# 0.0

cap_cam.release()
