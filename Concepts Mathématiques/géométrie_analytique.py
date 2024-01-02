# La géométrie analytique, développée par Descartes et Fermat, utilise des équations
# pour décrire des formes géométriques via un système de coordonnées. En 2D, le repère
# est noté (O, i, j) et en 3D, un axe supplémentaire k est ajouté. Cette méthode
# permet la représentation de figures comme les droites et les cercles, avec des
# équations telles que y = ax + b pour une droite. L'intégration de l'analyse
# mathématique offre des outils puissants pour la dérivation et la résolution de
# problèmes, et s'adapte bien Ã  la programmation pour l”étude des courbes
# définies par des équations.

from math import pi, cos, sin
from collections import namedtuple
import matplotlib.pyplot as plt
from numpy import linspace


plt.style.use('grayscale')

# Création d’une classe pour gérer les points
Point = namedtuple('Point', 'x y')

# Positionnement de points dans un plan 2D
O = Point(0.0, 0.0)
P0 = Point(1, 1)
P1 = Point(1.2, 1.2)

plt.scatter(O.x, O.y)
plt.scatter(P0.x, P0.y)
plt.scatter(P1.x, P1.y)

plt.annotate('O', (O.x, O.y))
plt.annotate('P0', (P0.x, P0.y))
plt.annotate('P1', (P1.x, P1.y))
plt.grid()
plt.show()

# Calcul des points d’une droite
# dont la pente est a = 2 et dont l’intersection
# avec l’axe des ordonnées se fait en b = 1
a = 2
b = 1
D = lambda x: a * x + b

X = list(linspace(-2, 2, 100))
Y = [D(x) for x in X]
plt.plot(X, Y, label='Droite D')
plt.legend()
plt.grid()
plt.show()

# Calcul des points d’une spirale logarithmique
Theta = list(linspace(0, 8 * pi, 200))
a = 1
b = 1.3
X = [a * (b ** theta) * cos(theta) for theta in Theta]
Y = [a * (b ** theta) * sin(theta) for theta in Theta]

plt.plot(X, Y, label='Spirale S')
plt.legend()
plt.grid()
plt.show()
