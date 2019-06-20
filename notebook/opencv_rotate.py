import cv2

img = cv2.imread('data/src/lena.jpg')
print(type(img))
# <class 'numpy.ndarray'>

print(img.shape)
# (225, 400, 3)

img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('data/dst/lena_cv_rotate_90_clockwise.jpg', img_rotate_90_clockwise)
# True

img_rotate_90_counterclockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('data/dst/lena_cv_rotate_90_counterclockwise.jpg', img_rotate_90_counterclockwise)
# True

img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imwrite('data/dst/lena_cv_rotate_180.jpg', img_rotate_180)
# True
