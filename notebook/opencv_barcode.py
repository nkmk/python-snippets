import cv2

print(cv2.__version__)
# 4.6.0

img = cv2.imread('data/src/barcode.jpg')

bd = cv2.barcode.BarcodeDetector()
# bd = cv2.barcode.BarcodeDetector('path/to/sr.prototxt', 'path/to/sr.caffemodel')

retval, decoded_info, decoded_type, points = bd.detectAndDecode(img)

print(retval)
# True

print(decoded_info)
# ('1923055034006', '9784873117980')

print(decoded_type)
# (2, 2)

print(cv2.barcode.EAN_13)
# 2

print(type(points))
# <class 'numpy.ndarray'>

print(points)
# [[[142.38849 221.83641]
#   [156.36218 172.35411]
#   [356.90564 228.98714]
#   [342.93195 278.46942]]
# 
#  [[180.30583 128.89304]
#   [191.59013  88.83808]
#   [371.00458 139.38284]
#   [359.72028 179.4378 ]]]

print(points.shape)
# (2, 4, 2)

img = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 3)

for s, p in zip(decoded_info, points):
    img = cv2.putText(img, s, p[1].astype(int),
                      cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imwrite('data/dst/barcode_opencv.jpg', img)
# True
