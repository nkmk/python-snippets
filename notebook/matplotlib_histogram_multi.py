from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('data/src/lenna_square.png')

r = np.array(im)[:, :, 0].flatten()
g = np.array(im)[:, :, 1].flatten()
b = np.array(im)[:, :, 2].flatten()

bins_range = range(0, 257, 8)
xtics_range = range(0, 257, 32)

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)

ax0.hist(r, bins=bins_range, color='r')
ax1.hist(g, bins=bins_range, color='g')
ax2.hist(b, bins=bins_range, color='b')

plt.setp((ax0, ax1, ax2), xticks=xtics_range, xlim=(0, 256))
ax0.grid(True)
ax1.grid(True)
ax2.grid(True)

plt.savefig("data/dst/matplotlib_histogram_multi.png")
