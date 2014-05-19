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

# On enlève la barre d'outils
matplotlib.rcParams['toolbar'] = 'None'

# L'image  est stockée dans uns tableau de numpy  de taille (512,512,3)
RGB = read_png('lena.png')

# On récupère la taille de l'image (attention à l'ordre)
height, width = RGB.shape[:2]

# On fixe in DPI
dpi = 72.0

# On calcule la taille de la figure correspondant à l'image
figsize= width/float(dpi), height/float(dpi)

# On crée la figure
fig = plt.figure(figsize=figsize, dpi=dpi, facecolor="white")

# On demande un cadre dont la taille est l'e,semble de la figure
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False)

# On affiche l'image (zorder=0)
ax.imshow(RGB, interpolation='nearest')

# On pixelize l'image
n = 16
RGB = RGB[::n,::n,:]
RGB = np.repeat(RGB,n, axis=0)
RGB = np.repeat(RGB,n, axis=1)

# On créé un disque qui va servir pour "clipper" l'image
patch = patches.Circle((.55,.45), radius=.25, transform=ax.transAxes,
                        facecolor='None', edgecolor='None',zorder=1)

# On affiche l'image pixelizée et clippée
ax.imshow(RGB, cmap=plt.cm.gray, zorder=3, interpolation='nearest', clip_path=patch)

# On affiche un cercle autour de l'image clippée
patch = patches.Circle((.55,.45), radius=.25, transform=ax.transAxes,
                       lw=1, facecolor='none', edgecolor='black', zorder=2)
ax.add_patch(patch)

# On enlève les repères sur les axes
ax.set_xticks([]), ax.set_yticks([])

# On sauve l'image
plt.savefig("lena-pixelated.png", dpi=dpi)

# On affiche l'image
plt.show()
