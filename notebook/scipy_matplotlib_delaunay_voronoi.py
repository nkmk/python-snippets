from scipy.spatial import Delaunay, delaunay_plot_2d, Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import numpy as np

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

tri = Delaunay(pts)

print(type(tri))
# <class 'scipy.spatial.qhull.Delaunay'>

fig = delaunay_plot_2d(tri)
fig.savefig('data/dst/scipy_matplotlib_delaunay.png')
plt.close()

# ![data/dst/scipy_matplotlib_delaunay.png](data/dst/scipy_matplotlib_delaunay.png)

print(tri.points)
# [[172.  47.]
#  [117. 192.]
#  [323. 251.]
#  [195. 359.]
#  [  9. 211.]
#  [277. 242.]]

print(tri.points == pts)
# [[ True  True]
#  [ True  True]
#  [ True  True]
#  [ True  True]
#  [ True  True]
#  [ True  True]]

print(tri.simplices)
# [[0 1 4]
#  [1 3 4]
#  [5 0 2]
#  [5 1 0]
#  [3 5 2]
#  [5 3 1]]

print(pts[tri.simplices])
# [[[172  47]
#   [117 192]
#   [  9 211]]
# 
#  [[117 192]
#   [195 359]
#   [  9 211]]
# 
#  [[277 242]
#   [172  47]
#   [323 251]]
# 
#  [[277 242]
#   [117 192]
#   [172  47]]
# 
#  [[195 359]
#   [277 242]
#   [323 251]]
# 
#  [[277 242]
#   [195 359]
#   [117 192]]]

vor = Voronoi(pts)

print(type(vor))
# <class 'scipy.spatial.qhull.Voronoi'>

fig = voronoi_plot_2d(vor)
fig.savefig('data/dst/scipy_matplotlib_voronoi.png')
plt.close()

# ![data/dst/scipy_matplotlib_voronoi.png](data/dst/scipy_matplotlib_voronoi.png)

print(vor.vertices)
# [[ 41.71518987  80.51265823]
#  [ 82.09150528 310.02013526]
#  [331.19719626  87.04766355]
#  [218.67630058 147.63583815]
#  [282.99117647 333.43398693]
#  [182.6014461  263.07537248]]

print(vor.regions)
# [[-1, 0, 1], [], [5, 3, 2, 4], [3, 0, -1, 2], [4, -1, 2], [5, 1, 0, 3], [5, 1, -1, 4]]

print([r for r in vor.regions if -1 not in r and r])
# [[5, 3, 2, 4], [5, 1, 0, 3]]

for region in [r for r in vor.regions if -1 not in r and r]:
    print(vor.vertices[region])
# [[182.6014461  263.07537248]
#  [218.67630058 147.63583815]
#  [331.19719626  87.04766355]
#  [282.99117647 333.43398693]]
# [[182.6014461  263.07537248]
#  [ 82.09150528 310.02013526]
#  [ 41.71518987  80.51265823]
#  [218.67630058 147.63583815]]

fig, ax = plt.subplots()
voronoi_plot_2d(vor, ax)

for region, c in zip([r for r in vor.regions if -1 not in r and r], ['yellow', 'pink']):
    ax.fill(vor.vertices[region][:, 0],
            vor.vertices[region][:, 1],
            color=c)

fig.savefig('data/dst/scipy_matplotlib_voronoi_fill.png')
plt.close()
# /usr/local/lib/python3.7/site-packages/scipy/spatial/_plotutils.py:20: MatplotlibDeprecationWarning: The ishold function was deprecated in version 2.0.
#   was_held = ax.ishold()

# ![data/dst/scipy_matplotlib_voronoi_fill.png](data/dst/scipy_matplotlib_voronoi_fill.png)

fig, ax = plt.subplots(figsize=(4, 4))
delaunay_plot_2d(tri, ax)
voronoi_plot_2d(vor, ax, show_vertices=False)

ax.set_xlim(0, w)
ax.set_ylim(0, h)
ax.grid(linestyle='--')

fig.savefig('data/dst/scipy_matplotlib_delaunay_voronoi.png')
plt.close()
# /usr/local/lib/python3.7/site-packages/scipy/spatial/_plotutils.py:20: MatplotlibDeprecationWarning: The ishold function was deprecated in version 2.0.
#   was_held = ax.ishold()

# ![data/dst/scipy_matplotlib_delaunay_voronoi.png](data/dst/scipy_matplotlib_delaunay_voronoi.png)
