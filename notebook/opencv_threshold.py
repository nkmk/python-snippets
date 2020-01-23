import cv2

im = cv2.imread('data/src/lena_square_half.png')

th, im_th = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)

print(th)
# 128.0

cv2.imwrite('data/dst/opencv_th.jpg', im_th)
# True

th, im_th_tz = cv2.threshold(im, 128, 255, cv2.THRESH_TOZERO)

print(th)
# 128.0

cv2.imwrite('data/dst/opencv_th_tz.jpg', im_th_tz)
# True

# th, im_th_otsu = cv2.threshold(im, 128, 192, cv2.THRESH_OTSU)
# error: OpenCV(4.2.0) /tmp/opencv-20200105-17262-cwpzm4/opencv-4.2.0/modules/imgproc/src/thresh.cpp:1529: error: (-215:Assertion failed) src.type() == CV_8UC1 in function 'threshold'

im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

th, im_gray_th_otsu = cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)

print(th)
# 117.0

cv2.imwrite('data/dst/opencv_th_otsu.jpg', im_gray_th_otsu)
# True
