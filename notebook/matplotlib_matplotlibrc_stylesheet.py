# %matplotlib inline

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# print(mpl.get_configdir())

print(mpl.matplotlib_fname())
# /usr/local/lib/python3.6/site-packages/matplotlib/mpl-data/matplotlibrc

print(plt.style.available)
# ['seaborn-dark', 'seaborn-darkgrid', 'seaborn-ticks', 'fivethirtyeight', 'seaborn-whitegrid', 'classic', 'seaborn-talk', 'seaborn-dark-palette', 'seaborn-bright', 'seaborn-pastel', 'grayscale', 'seaborn-notebook', 'ggplot', 'seaborn-colorblind', 'seaborn-muted', 'seaborn', 'seaborn-paper', 'bmh', 'seaborn-white', 'dark_background', 'seaborn-poster', 'seaborn-deep']

x = np.arange(0, 2 * np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.savefig('data/dst/matplotlib_style_default.png')
plt.show()
# <matplotlib.figure.Figure at 0x10521ab38>

with plt.style.context('dark_background'):
    plt.plot(x, y)
    plt.savefig('data/dst/matplotlib_style_dark_background.png')
    plt.show()
# <matplotlib.figure.Figure at 0x10538e8d0>

with plt.style.context(['ggplot', 'dark_background']):
    plt.plot(x, y)
    plt.savefig('data/dst/matplotlib_style_ggplot_dark_background.png')
    plt.show()
# <matplotlib.figure.Figure at 0x10585bf60>

with plt.style.context('data/src/test.mplstyle'):
    plt.plot(x, y)
    plt.savefig('data/dst/matplotlib_style_test.png')
    plt.show()
# <matplotlib.figure.Figure at 0x10590afd0>

with plt.style.context(['ggplot', 'data/src/test.mplstyle']):
    plt.plot(x, y)
    plt.savefig('data/dst/matplotlib_style_test_ggplot.png')
    plt.show()
# <matplotlib.figure.Figure at 0x1059e5630>

plt.style.use('ggplot')
plt.plot(x, y)
plt.savefig('data/dst/matplotlib_style_ggplot.png')
plt.show()
# <matplotlib.figure.Figure at 0x105af8470>
