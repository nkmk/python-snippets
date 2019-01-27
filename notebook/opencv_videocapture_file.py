import cv2

cap_file = cv2.VideoCapture('data/temp/sample_video.mp4')
print(type(cap_file))
# <class 'cv2.VideoCapture'>

print(cap_file.isOpened())
# True

cap_file_wrong = cv2.VideoCapture('wrong_path')
print(type(cap_file_wrong))
# <class 'cv2.VideoCapture'>

print(cap_file_wrong.isOpened())
# False
