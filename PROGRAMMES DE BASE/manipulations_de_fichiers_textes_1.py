nom_fichier = input("Entrez le nom du fichier (avec l'extension .txt) : ")

while True:
    choix = input("Que voulez-vous faire ?\n\n1. Enregistrer de nouvelles lignes\n2. Afficher le contenu du "
                  "fichier\n3. Quitter\n\nChoisissez une option (1/2/3) : ")

    if choix == '1':
        nouvelles_lignes = []
        print("Entrez les lignes de texte. Appuyez simplement sur Enter pour terminer.")
        while True:
            ligne = input()
            if ligne:
                nouvelles_lignes.append(ligne)
            else:
                break

        with open(nom_fichier, 'a') as fichier:
            for ligne in nouvelles_lignes:
                fichier.write(ligne + '\n')
        print("Les lignes ont été enregistrées dans le fichier.")

    elif choix == '2':
        try:
            with open(nom_fichier, 'r') as fichier:
                contenu = fichier.read()
                print("Contenu du fichier :\n")
                print(contenu)
        except FileNotFoundError:
            print("Le fichier spécifié n'existe pas.")

    elif choix == '3':
        break

    else:
        print("Choix invalide. Veuillez choisir une option valide (1/2/3).")

print("Programme terminé.")
