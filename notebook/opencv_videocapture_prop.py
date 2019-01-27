import cv2

cap = cv2.VideoCapture('data/temp/sample_video.mp4')
print(type(cap))
# <class 'cv2.VideoCapture'>

print(cap.isOpened())
# True

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# 640.0

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# 360.0

print(cap.get(cv2.CAP_PROP_FPS))
# 29.97002997002997

print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# 360.0

print(cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS))
# 12.012

print(cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320))
# False

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# 640.0

print(cap.get(cv2.CAP_PROP_POS_FRAMES))
# 0.0

print(cap.set(cv2.CAP_PROP_POS_FRAMES, 100))
# True

print(cap.get(cv2.CAP_PROP_POS_FRAMES))
# 100.0
