import time
import random


# Algorithme de tri par sélection
def tri_selection(arr):
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    end_time = time.time()
    return arr, end_time - start_time


# Algorithme de tri à bulles
def tri_bulles(arr):
    start_time = time.time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end_time = time.time()
    return arr, end_time - start_time


# Algorithme de tri par insertion
def tri_insertion(arr):
    start_time = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    end_time = time.time()
    return arr, end_time - start_time


def generer_liste_aleatoire(n):
    return [random.randint(1, 1000) for _ in range(n)]


def comparer_temps():
    n = 1000
    liste_test = generer_liste_aleatoire(n)

    liste_copie = liste_test.copy()
    tri_sel, temps_sel = tri_selection(liste_copie)

    liste_copie = liste_test.copy()
    tri_bul, temps_bul = tri_bulles(liste_copie)

    liste_copie = liste_test.copy()
    tri_ins, temps_ins = tri_insertion(liste_copie)

    liste_copie = liste_test.copy()
    start_time = time.time()
    liste_copie.sort()
    temps_sort = time.time() - start_time

    liste_copie = liste_test.copy()
    start_time = time.time()
    sorted_liste = sorted(liste_copie)
    temps_sorted = time.time() - start_time

    print(f"Tri par sélection - Temps d'exécution : {temps_sel:.6f} secondes")
    print(f"Tri à bulles - Temps d'exécution : {temps_bul:.6f} secondes")
    print(f"Tri par insertion - Temps d'exécution : {temps_ins:.6f} secondes")
    print(f"Méthode sort() - Temps d'exécution : {temps_sort:.6f} secondes")
    print(f"Méthode sorted() - Temps d'exécution : {temps_sorted:.6f} secondes")


comparer_temps()
