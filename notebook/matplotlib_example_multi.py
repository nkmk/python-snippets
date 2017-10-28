import numpy as np
import matplotlib.pyplot as plt

fig, ((ax00, ax01, ax02), (ax10, ax11, ax12)) = plt.subplots(nrows=2, ncols=3, sharey=True)

x = np.arange(4)

ax00.plot(x, x, 'ro--')
ax01.plot(x, x**1.5, 'g^-.')
ax02.plot(x, x**2, 'bs:')
ax10.bar(x, x + 1, width=0.5, align='center', color='r')
ax11.bar(x, x**1.5 + 1, width=0.5, align='center', color='g')
ax12.bar(x, x**2 + 1, width=0.5, align='center', color='b')

plt.rcParams['font.size'] = 10
plt.tight_layout()

plt.savefig("data/dst/matplotlib_example_multi.png")
