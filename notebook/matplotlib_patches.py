import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure()
ax = plt.axes()

# fc = face color, ec = edge color
c = patches.Circle(xy=(0, 0), radius=0.5, fc='g', ec='r')
e = patches.Ellipse(xy=(-0.25, 0), width=0.5, height=0.25, fc='b', ec='y')
r = patches.Rectangle(xy=(0, 0), width=0.25, height=0.5, ec='#000000', fill=False)
ax.add_patch(c)
ax.add_patch(e)
ax.add_patch(r)

plt.axis('scaled')
ax.set_aspect('equal')

plt.savefig('data/dst/matplotlib_patches.png')
