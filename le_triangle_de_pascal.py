lp = [1]
n = int(input("Saisir le nombre de lignes du tableau de Pascal = "))

for j in range(n):
    nl = lp + [1]
    for i in range(len(lp) - 1):
        nl[i + 1] = lp[i] + lp[i + 1]
    lp = nl
    print(nl)


def calculer_ligne_pascal(n):
    if n == 0:
        return [1]

    ligne_prec = calculer_ligne_pascal(n - 1)
    nouvelle_ligne = [1]

    for i in range(1, n):
        nouvelle_ligne.append(ligne_prec[i - 1] + ligne_prec[i])

    nouvelle_ligne.append(1)
    return nouvelle_ligne


def valeur_max_ligne_pascal(n):
    ligne_n = calculer_ligne_pascal(n)
    return max(ligne_n)


n = int(input("Entrez le numéro de ligne n : "))

max_valeur = valeur_max_ligne_pascal(n)

print("La valeur maximale dans la ligne {} du triangle de Pascal est : {}".format(n, max_valeur))
