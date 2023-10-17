import random


def mode_solo():
    limite_superieure = int(input("Choisissez la limite supérieure de l'intervalle (par exemple, 100) : "))
    nombre_secret = random.randint(1, limite_superieure)

    essais = 0
    while True:
        essais += 1
        try:
            proposition = int(input(f"Devinez le nombre entre 1 et {limite_superieure} : "))

            if proposition < 1 or proposition > limite_superieure:
                print(f"Le nombre doit être entre 1 et {limite_superieure}. Essayez encore.")
            elif proposition < nombre_secret:
                print("Trop petit ! Essayez encore.")
            elif proposition > nombre_secret:
                print("Trop grand ! Essayez encore.")
            else:
                print(f"Félicitations ! Vous avez trouvé le nombre {nombre_secret} en {essais} essais.")
                return essais
        except ValueError:
            print(f"Veuillez entrer un nombre valide entre 1 et {limite_superieure}.")


def mode_multijoueur():
    nombre_secret = int(input("Joueur 1, entrez le nombre à deviner (entre 1 et 100) : "))
    essais = 0
    while True:
        essais += 1
        try:
            proposition = int(input("Joueur 2, devinez le nombre : "))

            if proposition < 1 or proposition > 100:
                print("Le nombre doit être entre 1 et 100. Essayez encore.")
            elif proposition < nombre_secret:
                print("Trop petit ! Essayez encore.")
            elif proposition > nombre_secret:
                print("Trop grand ! Essayez encore.")
            else:
                print(f"Félicitations, Joueur 2 ! Vous avez trouvé le nombre {nombre_secret} en {essais} essais.")
                return essais
        except ValueError:
            print("Veuillez entrer un nombre valide entre 1 et 100.")


print("Bienvenue dans le jeu de devinette !")
score_total = 0

while True:
    print("Choisissez un mode de jeu :")
    print("1. Mode Solo")
    print("2. Mode Multijoueur")
    print("3. Quitter")
    choix_mode = input("Entrez le numéro du mode que vous souhaitez jouer (ou 3 pour quitter) : ")

    if choix_mode == "1":
        score_partie_solo = mode_solo()
        score_total += score_partie_solo
        print(f"Score de la partie solo : {score_partie_solo}")
    elif choix_mode == "2":
        score_partie_multijoueur = mode_multijoueur()
        score_total += score_partie_multijoueur
        print(f"Score de la partie multijoueur : {score_partie_multijoueur}")

    if choix_mode != "3":
        continuer = input("Voulez-vous refaire une partie ? (Oui/Non) : ")
        if continuer.lower() != "oui":
            break
    else:
        break

print(f"Score total : {score_total}")
