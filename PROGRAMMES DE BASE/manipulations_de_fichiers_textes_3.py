nom_fichier_source = input("Entrez le nom du fichier (avec l'extension .txt) : ")
nouvelles_lignes = []
print("Entrez les lignes de texte. Appuyez simplement sur Enter pour terminer.")
while True:
    ligne = input()
    if ligne:
        nouvelles_lignes.append(ligne)
    else:
        break

with open(nom_fichier_source, 'a') as fichier:
    for ligne in nouvelles_lignes:
        fichier.write(ligne + '\n')
print("Les lignes ont été enregistrées dans le fichier.")

nom_fichier_destination = input("Entrez le nom du fichier de destination : ")

with open(nom_fichier_source, 'r') as fichier_source:
    contenu = fichier_source.read()

contenu_modifie = contenu.replace(' ', '   ')

with open(nom_fichier_destination, 'w') as fichier_destination:
    fichier_destination.write(contenu_modifie)

print("Le fichier a été recopié avec les espaces triplés et enregistré sous", nom_fichier_destination)
