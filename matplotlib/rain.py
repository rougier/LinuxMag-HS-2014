# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import matplotlib
import numpy as np
matplotlib.rcParams['toolbar'] = 'None'
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation


width, height = 512,512
dpi = 72.0
figsize = width/float(dpi), height/float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.patch.set_facecolor('white')
ax = fig.add_axes([0,0,1,1], frameon=False, aspect=1)

XY = np.random.uniform(0,1,(50,2))
C = np.ones((50,4)) * (0,0,0,1)
C[:,3] = np.linspace(0,1,50)
S = np.linspace(50,50*50, 50)
scat = ax.scatter(XY[:,0], XY[:,1], s=S, lw = 0.5,
                  edgecolors = C, facecolors='None')
ax.set_xlim(0,1), ax.set_xticks([])
ax.set_ylim(0,1), ax.set_yticks([])


def update(frame):
    global XY, C, S

    i = frame % 50
    C[:,3] = np.maximum(0, C[:,3]-0.02)
    S += 250
    XY[i] = np.random.uniform(0,1,2)
    S[i] = 50
    C[i,3] = 1
    scat.set_edgecolors(C)
    scat.set_sizes(S)
    scat.set_offsets(XY)
    return scat,

animation = FuncAnimation(fig, update, interval=10)
# animation.save('rain.gif', writer='imagemagick', fps=30, dpi=dpi/2)
# plt.savefig("rain.png", dpi=dpi)
plt.show()
