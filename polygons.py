"""
============================
Circles, Wedges and Polygons
============================

This example demonstrates how to use
:class:`patch collections<~.collections.PatchCollection>`.
"""

import numpy as np
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt


fig, ax = plt.subplots()


# vertices
N = 3
r = 1.0
angs = [i*2*np.pi/N for i in range(N)] 
verts = [(r*np.cos(a), r*np.sin(a)) for a in angs]
verts = np.array(verts)

ax.scatter(verts[:, 0], verts[:, 1])

print(angs, verts)

# create polygon



# circle
angs = np.linspace(0, 2*np.pi, 100)
verts = np.array([(r*np.cos(a), r*np.sin(a)) for a in angs])
ax.plot(verts[:, 0], verts[:, 1])

plt.axis('equal')
plt.show()

