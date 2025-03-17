def cherche_ville(ville_a_chercher, dict_pays):
    for pays in dict_pays:
        if ville_a_chercher in dict_pays[pays]:
            return f'{ville_a_chercher} se trouve en {pays}'
    return f'{ville_a_chercher} n\'a pas été trouvée'