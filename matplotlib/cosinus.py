# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# Création d'une figure de taille 8x6 (points) en utilisant un DPI de 80
fig = plt.figure(figsize=(8,6), dpi=80)

# Création d'une sous-figure
ax = plt.subplot(1,1,1)

# Création de X et Y
X = np.linspace(0, 2*np.pi, 256)
Y = np.cos(X)

# Affichage de la courbe en bleu, épaisseur 1, trait continu
ax.plot(X, Y, color="blue", linewidth=1.0, linestyle="-")

# Limites en abscisse
ax.set_xlim(0,2*np.pi)

# Indicateurs sur les abscisses
ax.set_xticks(np.linspace(0,6,6, endpoint=True))

# Limites en abscisse
ax.set_ylim(-1.0,1.0)

# Indicateurs sur les ordnonnées
ax.set_yticks(np.linspace(-1,1,5,endpoint=True))

# On sauve a figure
plt.savefig('cosinus.png', dpi=72)

# Affiche la figure
plt.show()
