def remplir_dict(dictionnaire):
    nom = input("Entrez le nom de l'individu : ")
    age = int(input("Entrez l'âge de l'individu en années : "))
    sexe = input("Entrez le sexe de l'individu (F/M) : ").upper()
    taille = float(input("Entrez la taille de l'individu en mètres : "))

    dictionnaire[nom] = (age, sexe, taille)


def consulter_dict(dictionnaire):
    nom = input("Entrez le nom de l'individu à consulter : ")

    if nom in dictionnaire:
        age, sexe, taille = dictionnaire[nom]
        print(f"Nom : {nom} - âge : {age} ans - sexe : {sexe} - taille : {taille} m")
    else:
        print("L'individu n'existe pas dans le dictionnaire.")


def sauvegarder_dict(dictionnaire, nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        for nom, (age, sexe, taille) in dictionnaire.items():
            fichier.write(f"{nom},{age},{sexe},{taille}\n")


def charger_dict(nom_fichier):
    dictionnaire = {}
    try:
        with open(nom_fichier, 'r') as fichier:
            for ligne in fichier:
                nom, age, sexe, taille = ligne.strip().split(',')
                dictionnaire[nom] = (int(age), sexe, float(taille))
    except FileNotFoundError:
        pass
    return dictionnaire


nom_fichier = 'individus.txt'
dictionnaire = charger_dict(nom_fichier)


def main():
    while True:
        print("\nMenu :")
        print("1. Ajouter des informations")
        print("2. Consulter des informations")
        print("3. Quitter")

        choix = input("Que souhaitez-vous faire ? (1/2/3) : ")

        if choix == '1':
            remplir_dict(dictionnaire)
        elif choix == '2':
            consulter_dict(dictionnaire)
        elif choix == '3':
            sauvegarder_dict(dictionnaire, nom_fichier)
            print("Le dictionnaire a été sauvegardé dans", nom_fichier)
            break
        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")


main()
