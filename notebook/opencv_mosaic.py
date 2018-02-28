import cv2

src = cv2.imread('data/src/lena.jpg')

def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

dst_01 = mosaic(src)
cv2.imwrite('data/dst/opencv_mosaic_01.jpg', dst_01)

dst_005 = mosaic(src, ratio=0.05)
cv2.imwrite('data/dst/opencv_mosaic_005.jpg', dst_005)
# True

def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst

dst_area = mosaic_area(src, 100, 50, 100, 150)
cv2.imwrite('data/dst/opencv_mosaic_area.jpg', dst_area)
# True

face_cascade_path = '/usr/local/opt/opencv/share/'\
                    'OpenCV/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_path)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(src_gray)

for x, y, w, h in faces:
    dst_face = mosaic_area(src, x, y, w, h)

cv2.imwrite('data/dst/opencv_mosaic_face.jpg', dst_face)
# True
