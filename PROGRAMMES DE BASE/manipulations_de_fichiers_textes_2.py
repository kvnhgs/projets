with open('tables_de_multiplication.txt', 'w') as fichier:
    for multiplicateur in range(2, 31):
        table = [multiplicateur * i for i in range(1, 21)]
        fichier.write(f"Table de multiplication de {multiplicateur} :\n")
        for i, resultat in enumerate(table):
            fichier.write(f"{multiplicateur} x {i + 1} = {resultat}\n")
        fichier.write("\n")

with open('tables_de_multiplication.txt', 'r') as fichier:
    contenu = fichier.read()
    print(contenu)
