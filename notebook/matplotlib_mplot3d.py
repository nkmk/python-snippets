import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = y = np.arange(-15, 15, 0.5)
X, Y = np.meshgrid(x, y)

sigma = 4
Z = np.exp(-(X**2 + Y**2)/(2*sigma**2)) / (2*np.pi*sigma**2)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
plt.savefig("data/dst/matplotlib_mplot3d_surface.png")

ax.clear()
ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
plt.savefig("data/dst/matplotlib_mplot3d_wireframe.png")

ax.clear()
ax.scatter(X, Y, Z, s=1)
plt.savefig("data/dst/matplotlib_mplot3d_scatter.png")
