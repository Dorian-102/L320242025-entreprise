def searchL(element, liste):
    for index, valeur in enumerate(liste):
        if element == valeur:
            return index
    return False

ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

element_a_trouver = 5
print(searchL(element_a_trouver, ma_liste))

resultat = searchL(element_a_trouver, ma_liste)
print(f'L\'élément {element_a_trouver} se trouve à l\'index {resultat}.')

element_a_trouver = 11
resultat = searchL(element_a_trouver, ma_liste)
if resultat == False:
    print(f"L'élément {element_a_trouver} n'est pas dans la liste.")

if not resultat:
    print(f"L'élément {element_a_trouver} n'est pas dans la liste.")
    

