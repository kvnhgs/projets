def echange_cles_valeurs(dictionnaire):
    nouveau_dictionnaire = {valeur: cle for cle, valeur in dictionnaire.items()}
    return nouveau_dictionnaire


dictionnaire_anglais_francais = {
    'Kévin': 'Kévin',
    'is': 'est',
    'the': 'le',
    'new': 'nouveau',
    'delegate': 'délégué'
}

dictionnaire_francais_anglais = echange_cles_valeurs(dictionnaire_anglais_francais)

dictionnaire_francais_anglais
