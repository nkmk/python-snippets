# %matplotlib inline

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2 * np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.savefig('data/dst/matplotlib_style_default.png')
plt.show()
# <matplotlib.figure.Figure at 0x10baf68d0>

with plt.style.context('classic'):
    plt.plot(x, y)
    plt.savefig('data/dst/matplotlib_style_classic.png')
    plt.show()
# <matplotlib.figure.Figure at 0x10bc10668>

# mpl.rcParams['axes.autolimit_mode'] = 'round_numbers'
mpl.rcParams['axes.xmargin'] = 0
mpl.rcParams['axes.ymargin'] = 0

plt.plot(x, y)
plt.savefig('data/dst/matplotlib_style_change_axes_margin.png')
plt.show()
# <matplotlib.figure.Figure at 0x10c0acf98>
