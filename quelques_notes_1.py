def calculer_moyenne(notes):
    if len(notes) == 0:
        return 0.0
    return sum(notes) / len(notes)


notes = []

while True:
    note_str = input("Entrez une note sur 20 (ou appuyez sur Entrée pour terminer) : ")

    if note_str == "":
        break

    try:
        note = float(note_str)
    except ValueError:
        print("Veuillez entrer une note valide.")
        continue

    if 0 <= note <= 20:
        notes.append(note)
    else:
        print("La note doit être comprise entre 0 et 20.")

if len(notes) > 0:
    nombre_de_notes = len(notes)
    note_max = max(notes)
    note_min = min(notes)
    moyenne = calculer_moyenne(notes)

    print(f"Nombre de notes entrées : {nombre_de_notes}")
    print(f"Note la plus élevée : {note_max}")
    print(f"Note la plus basse : {note_min}")
    print(f"Moyenne de toutes les notes : {moyenne:.2f}")
else:
    print("Aucune note n'a été entrée.")
