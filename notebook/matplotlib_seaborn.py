import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
sns.set_context("paper", 1.5, {"lines.linewidth": 4})
sns.set_palette("winter_r", 8, 1)
sns.set('talk', 'whitegrid', 'dark', font_scale=1.5,
        rc={"lines.linewidth": 2, 'grid.linestyle': '--'})

x = np.arange(0, 2.1, 0.1)

plt.plot(x, x)
plt.plot(x, x**1.5)
plt.plot(x, x**2)

plt.savefig('data/dst/matplotlib_seaborn_set_all.png')
