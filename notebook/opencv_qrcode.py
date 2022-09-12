import cv2

print(cv2.__version__)
# 4.6.0

img = cv2.imread('data/src/qrcode.png')

qcd = cv2.QRCodeDetector()

retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)

print(retval)
# True

print(decoded_info)
# ('QR Code Two', '', 'QR Code One')

print(type(points))
# <class 'numpy.ndarray'>

print(points)
# [[[290.9108    106.20954  ]
#   [472.8162      0.8958926]
#   [578.5836    184.1002   ]
#   [396.0495    287.81277  ]]
# 
#  [[620.         40.       ]
#   [829.         40.       ]
#   [829.        249.       ]
#   [620.        249.       ]]
# 
#  [[ 40.         40.       ]
#   [249.         40.       ]
#   [249.        249.       ]
#   [ 40.        249.       ]]]

print(points.shape)
# (3, 4, 2)

print(type(straight_qrcode))
# <class 'tuple'>

print(type(straight_qrcode[0]))
# <class 'numpy.ndarray'>

print(straight_qrcode[0].shape)
# (21, 21)

img = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 3)

for s, p in zip(decoded_info, points):
    img = cv2.putText(img, s, p[0].astype(int),
                      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imwrite('data/dst/qrcode_opencv.jpg', img)
# True
