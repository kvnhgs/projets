def fonction_les_impairs(nombre1, nombre2):
    if nombre1 > nombre2:
        nombre1, nombre2 = nombre2, nombre1
    if nombre1 % 2 == 0:
        nombre1 += 1
    for i in range(nombre1, nombre2, 2):
        print(i)


fonction_les_impairs(2, 10)
