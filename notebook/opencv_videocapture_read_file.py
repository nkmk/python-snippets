import cv2

cap = cv2.VideoCapture('data/temp/sample_video.mp4')
print(type(cap))
# <class 'cv2.VideoCapture'>

print(cap.isOpened())
# True

print(cap.get(cv2.CAP_PROP_POS_FRAMES))
# 0.0

print(cap.get(cv2.CAP_PROP_POS_MSEC))
# 0.0

ret, frame = cap.read()

print(ret)
# True

print(type(frame))
# <class 'numpy.ndarray'>

print(frame.shape)
# (360, 640, 3)

print(cap.get(cv2.CAP_PROP_POS_FRAMES))
# 1.0

print(cap.get(cv2.CAP_PROP_POS_MSEC))
# 33.36666666666667

print(1 / cap.get(cv2.CAP_PROP_FPS) * 1000)
# 33.36666666666667

cap.set(cv2.CAP_PROP_POS_FRAMES, 100)
print(cap.get(cv2.CAP_PROP_POS_FRAMES))
# 100.0

ret, frame = cap.read()

print(ret)
# True

print(cap.get(cv2.CAP_PROP_POS_FRAMES))
# 101.0

print(cap.get(cv2.CAP_PROP_POS_MSEC))
# 3370.0333333333333

cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(cap.get(cv2.CAP_PROP_POS_FRAMES))
# 360.0

ret, frame = cap.read()

print(ret)
# False

print(frame)
# None

print(cap.get(cv2.CAP_PROP_POS_FRAMES))
# 360.0

cap.set(cv2.CAP_PROP_POS_FRAMES, 1000)
print(cap.get(cv2.CAP_PROP_POS_FRAMES))
# 360.0
