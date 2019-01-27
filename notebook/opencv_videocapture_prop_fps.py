import cv2

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FPS))
# 29.000049

print(cap.set(cv2.CAP_PROP_FPS, 10))
# True

print(cap.get(cv2.CAP_PROP_FPS))
# 10.0

print(cap.set(cv2.CAP_PROP_FPS, 120))
# True

print(cap.get(cv2.CAP_PROP_FPS))
# 30.00003

cap.release()
