import cv2
from PIL import Image

def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

src = cv2.cvtColor(cv2.imread('data/src/lena.jpg'), cv2.COLOR_BGR2RGB)

imgs = [Image.fromarray(mosaic(src, 1 / i)) for i in range(1, 25)]
imgs += imgs[-2::-1] + [Image.fromarray(src)] * 5

imgs[0].save('data/temp/opencv_mosaic.gif',
             save_all=True, append_images=imgs[1:], optimize=False, duration=50, loop=0)
