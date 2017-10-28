import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2.0, 20)

plt.plot(x, x, 'b:')
plt.plot(x, x**1.5, 'rs-')
plt.plot(x, x**2, color='#30F050', marker='^', markerfacecolor='blue', markeredgecolor='blue')

plt.tight_layout()

plt.savefig("data/dst/matplotlib_example_single.png")
