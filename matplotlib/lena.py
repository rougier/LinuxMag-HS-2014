# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib._png import read_png

# No toolbar
matplotlib.rcParams['toolbar'] = 'None'

# Read the image into a de numpy array (shape = (512,512,3))
RGB = read_png('lena.png')

# Get image size (be careful with order)
height, width = RGB.shape[:2]

# Set DPI
dpi = 72.0

# Set  figure size / image
figsize= width/float(dpi), height/float(dpi)

# Figure creation
fig = plt.figure(figsize=figsize, dpi=dpi, facecolor="white")

# Set axes on the whole figure
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False)

# Display image
ax.imshow(RGB, interpolation='nearest')

# Pixelate image
n = 16
RGB = RGB[::n,::n,:]
RGB = np.repeat(RGB,n, axis=0)
RGB = np.repeat(RGB,n, axis=1)

# Mask creation
patch = patches.Circle((.55,.45), radius=.25, transform=ax.transAxes,
                        facecolor='None', edgecolor='None',zorder=1)

# Display clipped pixelated image
ax.imshow(RGB, cmap=plt.cm.gray, zorder=3, interpolation='nearest', clip_path=patch)

# Add a circle around
patch = patches.Circle((.55,.45), radius=.25, transform=ax.transAxes,
                       lw=1, facecolor='none', edgecolor='black', zorder=2)
ax.add_patch(patch)

# remove ticks
ax.set_xticks([]), ax.set_yticks([])

# Save image
plt.savefig("lena-pixelated.png", dpi=dpi)

# Displya figure
plt.show()
