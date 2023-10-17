def convertir_secondes(secondes):
    annees = secondes // 31536000
    reste = secondes % 31536000
    mois = reste // 2592000
    reste = reste % 2592000
    jours = reste // 86400
    reste = reste % 86400
    heures = reste // 3600
    reste = reste % 3600
    minutes = reste // 60
    secondes = reste % 60
    return annees, mois, jours, heures, minutes, secondes


def convertir_vitesse(mph):
    mps = mph * 0.44704
    kmh = mph * 1.60934
    return mps, kmh


secondes = int(input("Entrez un nombre de secondes : "))

annees, mois, jours, heures, minutes, secondes = convertir_secondes(secondes)

print(f"{secondes} secondes correspondent à :")
print(f"{annees} années {mois} mois {jours} jours")
print(f"{heures} heures {minutes} minutes {secondes} secondes")

mph = float(input("Entrez une vitesse en miles/heure : "))

mps, kmh = convertir_vitesse(mph)

print(f"{mph} miles/heure équivaut à {mps:.2f} mètres/seconde et {kmh:.2f} km/h")
