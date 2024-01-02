# L'identité d'Euler, e^(i*pi) + 1 = 0, est considérée comme l'une des formules
# mathématiques les plus belles, combinant les constantes fondamentales e, i, pi, 1 et 0.
# Elle encapsule des éléments mathématiques essentiels : la constante e, l'unité imaginaire i,
# le nombre pi, l'unité 1 et le zéro 0.
# Le texte offre une perspective géométrique, mettant en valeur la beauté de la formule à travers
# une série de transformations dans le plan complexe, impliquant des rotations et des mises à l'échelle.
# Ces opérations illustrent comment la multiplication complexe peut être visualisée comme
# une homothétie suivie d'une rotation.
# Cela est davantage expliqué en utilisant la limite de (1 + x/n)^n lorsque n tend vers l'infini.
# En insérant x = i*pi, on montre que e^(i*pi) est le produit de n facteurs (1 + i*pi/n),
# conduisant à une interprétation géométrique de l'exponentiation complexe.
# Les rapports de réduction et les angles de rotation sont décrits en coordonnées polaires,
# aidant à comprendre les propriétés géométriques des nombres complexes, comme illustré
# par les relations entre les segments dans les triangles pythagoriciens.

import matplotlib.pyplot as plt
from math import pi, e

# Vérification de la formule d'Euler.
print((e**(1j * pi)).real)  # Doit être -1 et non 1, peut-être une erreur d'impression dans le texte.

# Intuition sur le sens de la formule et l'esthétique sous-jacente.
def plot_exponential_approximation(n):
    p_0 = 1 + 0j
    r = 1 + pi/n * 1j
    p_im1 = p_0
    p_i = p_0
    for i in range(0, n):
        print(p_i)
        plt.plot([0, p_i.real], [0, p_i.imag], 'r')  # Utilisez 'r' pour le rouge
        p_i = p_i * r
        plt.plot([p_im1.real, p_i.real], [p_im1.imag, p_i.imag], 'k')  # Utilisez 'k' pour le noir
        p_im1 = p_i
        plt.plot([0, p_i.real], [0, p_i.imag], 'k')  # Utilisez 'k' pour le noir
    plt.axis('equal')
    plt.show()

plot_exponential_approximation(10)
