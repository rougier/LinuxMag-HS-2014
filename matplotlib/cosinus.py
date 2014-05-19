# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Creation of a figure of size 8x6 (points) using DPI of 80
fig = plt.figure(figsize=(8,6), dpi=80)

# Creation of a sub-figure
ax = plt.subplot(1,1,1)

# Creation of X and Y
X = np.linspace(0, 2*np.pi, 256)
Y = np.cos(X)

# Display of blue curve, linewidht 1
ax.plot(X, Y, color="blue", linewidth=1.0, linestyle="-")

# x limits
ax.set_xlim(0,2*np.pi)

# x ticks
ax.set_xticks(np.linspace(0,6,6, endpoint=True))

# y limits
Limites en abscisse
ax.set_ylim(-1.0,1.0)

# y ticks
ax.set_yticks(np.linspace(-1,1,5,endpoint=True))

# Figure saving
plt.savefig('cosinus.png', dpi=72)

# Figure display
plt.show()
