import matplotlib.pyplot as plt
import numpy as np

ints = np.genfromtxt('intersections.csv', delimiter=',')
print(ints)

fig = plt.figure(figsize=(7,7), constrained_layout=True)
ax  = fig.add_subplot(111)

ax.scatter(ints[0],ints[1], s=0.1, marker='.', c='k', alpha=0.5) # type: ignore
ax.set_xlabel('c')
ax.set_ylabel('intersection-height')
plt.show()

