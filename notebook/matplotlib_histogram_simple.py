from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('data/src/lena_square.png')

r = np.array(im)[:, :, 0].flatten()
g = np.array(im)[:, :, 1].flatten()
b = np.array(im)[:, :, 2].flatten()

bins_range = range(0, 257, 8)
xtics_range = range(0, 257, 32)

plt.hist((r, g, b), bins=bins_range,
         color=['r', 'g', 'b'], label=['Red', 'Green', 'Blue'])
plt.legend(loc=2)

plt.grid(True)

[xmin, xmax, ymin, ymax] = plt.axis()
plt.axis([0, 256, 0, ymax])
plt.xticks(xtics_range)

plt.savefig("data/dst/matplotlib_histogram_single.png")
