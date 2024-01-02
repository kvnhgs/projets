# Planche de Galton - Démonstration de la distribution normale
# La Planche de Galton est un dispositif qui illustre la loi normale.
# Inventée par Sir Francis Galton, elle se compose de plusieurs rangées de clous.
# Les billes lâchées du sommet de la planche rebondissent aléatoirement sur les clous.
# Chaque rebond à gauche ou à droite est un événement aléatoire avec la même probabilité.
# La position finale des billes représente une distribution normale (courbe en cloche).
# La formule de la loi normale est donnée par f(x) = (1 / (σ * sqrt(2 * π))) * e ^ (-(x-μ)^2 / (2*σ^2))
# où μ est la moyenne et σ est l'écart-type de la distribution.
# En tombant à travers la planche, chaque bille a une chance égale de rebondir à gauche ou à droite.
# Avec un grand nombre de billes, la distribution des billes en bas suit la distribution normale.
# Cela démontre que même des processus aléatoires peuvent mener à une distribution prévisible.
# Le processus est aussi un bon exemple de la loi des grands nombres.
# La Planche de Galton est un outil pédagogique pour enseigner la statistique et la probabilité.


import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use('grayscale')

# Fonction galton_drop
def galton_drop(depth):
    nb_left = 0
    for i in range(0, depth):
        direction = np.random.choice(['L', 'R'])
        if direction == 'L':
            nb_left += 1
    return nb_left

# Fonction galton_board
def galton_board(nb_balls, depth):
    counter = {idx: 0 for idx in range(0, depth + 1)}
    for ball in range(nb_balls):
        nb_left = galton_drop(depth)
        counter[nb_left] += 1
    # Normalisation
    keys = list(counter.keys())
    for key in keys:
        counter[(key - depth / 2) / depth] = counter.pop(key) / nb_balls
    return counter

# Fonction draw_galton_board
def draw_galton_board(depth):
    X = []
    Y = []
    for step in range(0, depth):
        X += [-step / 2.0 + point for point in range(0, step + 1)]
        Y += [-step for _ in range(0, step + 1)]
    plt.scatter(X, Y, color='red')  # Changement de couleur ici
    plt.xlabel('Planche de Galton')
    plt.show()

# Exécution principale
depth = 30
counter = galton_board(20000, depth)
X = np.linspace(-0.6, 0.6, 100)
plt.bar(counter.keys(), counter.values(), label='nombre de billes par cellule', width=1.0 / (3 * depth), color='red')  # Changement de couleur ici
plt.plot(X, [1/math.sqrt(2 * math.pi) * math.exp(-1/2.0 * x**2) for x in X], color='black')  # Changement de couleur ici
plt.xlabel('cellules')
plt.legend()
plt.show()

print(max(counter.keys()))

draw_galton_board(10)
