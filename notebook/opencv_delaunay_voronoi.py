import cv2
import numpy as np

import pprint

w = h = 360

n = 6
np.random.seed(0)
pts = np.random.randint(0, w, (n, 2))

print(pts)
# [[172  47]
#  [117 192]
#  [323 251]
#  [195 359]
#  [  9 211]
#  [277 242]]

print(type(pts))
# <class 'numpy.ndarray'>

print(pts.shape)
# (6, 2)

img = np.zeros((w, h, 3), np.uint8)

for p in pts:
    cv2.drawMarker(img, tuple(p), (255, 255, 255), thickness=2)

cv2.imwrite('data/dst/opencv_random_pts.png', img)
# True

# ![data/dst/opencv_random_pts.png](data/dst/opencv_random_pts.png)

rect = (0, 0, w, h)

subdiv = cv2.Subdiv2D(rect)

for p in pts:
    subdiv.insert((p[0], p[1]))

triangles = subdiv.getTriangleList()

print(triangles)
# [[ 1080.     0.     0.  1080.   323.   251.]
#  [    0.  1080.  1080.     0. -1080. -1080.]
#  [    0.  1080. -1080. -1080.     9.   211.]
#  [-1080. -1080.  1080.     0.   172.    47.]
#  [  172.    47.  1080.     0.   323.   251.]
#  [  172.    47.   323.   251.   277.   242.]
#  [-1080. -1080.   172.    47.     9.   211.]
#  [  172.    47.   117.   192.     9.   211.]
#  [  117.   192.   172.    47.   277.   242.]
#  [    9.   211.   195.   359.     0.  1080.]
#  [  195.   359.     9.   211.   117.   192.]
#  [  323.   251.     0.  1080.   195.   359.]
#  [  195.   359.   117.   192.   277.   242.]
#  [  323.   251.   195.   359.   277.   242.]]

pols = triangles.reshape(-1, 3, 2)

print(pols)
# [[[ 1080.     0.]
#   [    0.  1080.]
#   [  323.   251.]]
# 
#  [[    0.  1080.]
#   [ 1080.     0.]
#   [-1080. -1080.]]
# 
#  [[    0.  1080.]
#   [-1080. -1080.]
#   [    9.   211.]]
# 
#  [[-1080. -1080.]
#   [ 1080.     0.]
#   [  172.    47.]]
# 
#  [[  172.    47.]
#   [ 1080.     0.]
#   [  323.   251.]]
# 
#  [[  172.    47.]
#   [  323.   251.]
#   [  277.   242.]]
# 
#  [[-1080. -1080.]
#   [  172.    47.]
#   [    9.   211.]]
# 
#  [[  172.    47.]
#   [  117.   192.]
#   [    9.   211.]]
# 
#  [[  117.   192.]
#   [  172.    47.]
#   [  277.   242.]]
# 
#  [[    9.   211.]
#   [  195.   359.]
#   [    0.  1080.]]
# 
#  [[  195.   359.]
#   [    9.   211.]
#   [  117.   192.]]
# 
#  [[  323.   251.]
#   [    0.  1080.]
#   [  195.   359.]]
# 
#  [[  195.   359.]
#   [  117.   192.]
#   [  277.   242.]]
# 
#  [[  323.   251.]
#   [  195.   359.]
#   [  277.   242.]]]

img_draw = img.copy()

cv2.polylines(img_draw, pols.astype(int), True, (0, 0, 255), thickness=2)

cv2.imwrite('data/dst/opencv_delaunay.png', img_draw)
# True

# ![data/dst/opencv_delaunay.png](data/dst/opencv_delaunay.png)

print(np.all(pols[:, :, 0] < w, axis=1))
# [False False  True False False  True  True  True  True  True  True  True
#   True  True]

pols_inner = pols[np.all(pols[:, :, 0] < w, axis=1) &
                  np.all(pols[:, :, 0] > 0, axis=1) &
                  np.all(pols[:, :, 1] < h, axis=1) &
                  np.all(pols[:, :, 1] > 0, axis=1)]

print(pols_inner)
# [[[172.  47.]
#   [323. 251.]
#   [277. 242.]]
# 
#  [[172.  47.]
#   [117. 192.]
#   [  9. 211.]]
# 
#  [[117. 192.]
#   [172.  47.]
#   [277. 242.]]
# 
#  [[195. 359.]
#   [  9. 211.]
#   [117. 192.]]
# 
#  [[195. 359.]
#   [117. 192.]
#   [277. 242.]]
# 
#  [[323. 251.]
#   [195. 359.]
#   [277. 242.]]]

img_draw = img.copy()

cv2.polylines(img_draw, pols_inner.astype(int), True, (0, 0, 255), thickness=2)

cv2.imwrite('data/dst/opencv_delaunay_inner.png', img_draw)
# True

# ![data/dst/opencv_delaunay_inner.png](data/dst/opencv_delaunay_inner.png)

facets, centers = subdiv.getVoronoiFacetList([])

pprint.pprint(facets)
# [array([[  331.1972 ,    87.04766],
#        [  218.6763 ,   147.63583],
#        [   41.71519,    80.51266],
#        [ -503.5626 ,  -461.44025],
#        [  540.8418 , -1621.6836 ],
#        [  618.2897 ,  -125.45706]], dtype=float32),
#  array([[218.6763 , 147.63583],
#        [182.60144, 263.07538],
#        [ 82.09151, 310.02014],
#        [ 41.71519,  80.51266]], dtype=float32),
#  array([[ 282.99118,  333.434  ],
#        [ 331.1972 ,   87.04766],
#        [ 618.2897 , -125.45706],
#        [ 987.2233 ,  987.2233 ],
#        [ 759.8912 ,  898.6488 ]], dtype=float32),
#  array([[ 182.60144,  263.07538],
#        [ 282.99118,  333.434  ],
#        [ 759.8912 ,  898.6488 ],
#        [-183.30182,  643.555  ],
#        [  82.09151,  310.02014]], dtype=float32),
#  array([[   82.09151,   310.02014],
#        [ -183.30182,   643.555  ],
#        [-1793.752  ,   626.876  ],
#        [ -503.5626 ,  -461.44025],
#        [   41.71519,    80.51266]], dtype=float32),
#  array([[218.6763 , 147.63583],
#        [331.1972 ,  87.04766],
#        [282.99118, 333.434  ],
#        [182.60144, 263.07538]], dtype=float32)]

print(centers)
# [[172.  47.]
#  [117. 192.]
#  [323. 251.]
#  [195. 359.]
#  [  9. 211.]
#  [277. 242.]]

img_draw = img.copy()

cv2.polylines(img_draw, [f.astype(int) for f in facets], True, (255, 255, 255), thickness=2)

cv2.imwrite('data/dst/opencv_voronoi.png', img_draw)
# True

# ![data/dst/opencv_voronoi.png](data/dst/opencv_voronoi.png)

img_draw = img.copy()

step = int(255 / len(facets))

for i, p in enumerate(f.astype(int) for f in facets):
    cv2.fillPoly(img_draw, [p], (step * i, step * i, step * i))

cv2.imwrite('data/dst/opencv_voronoi_fill.png', img_draw)
# True

# ![data/dst/opencv_voronoi_fill.png](data/dst/opencv_voronoi_fill.png)

img_draw = img.copy()

step = int(255 / len(facets))

for i, p in enumerate(f.astype(int) for f in facets):
    cv2.fillPoly(img_draw, [p], (step * i, step * i, step * i))

cv2.polylines(img_draw, pols_inner.astype(int), True, (0, 0, 255), thickness=2)

for c in centers:
    cv2.drawMarker(img_draw, tuple(c), (255, 255, 255), thickness=2)

cv2.imwrite('data/dst/opencv_delaunay_voronoi.png', img_draw)
# True

# ![data/dst/opencv_delaunay_voronoi.png](data/dst/opencv_delaunay_voronoi.png)
