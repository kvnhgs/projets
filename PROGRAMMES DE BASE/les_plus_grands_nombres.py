import random

liste_aleatoire = [random.randint(a=1, b=1000) for i in range(100)]

n_plus_grands = []
for i in range(10):
    max_element = max(liste_aleatoire)
    n_plus_grands.append(max_element)
    liste_aleatoire.remove(max_element)

n_plus_grands_sorted = sorted(n_plus_grands, reverse=True)

print("Les 10 plus grands éléments sont :", n_plus_grands)
print("")
print("Les 10 plus grands éléments sorted sont :", n_plus_grands_sorted)
