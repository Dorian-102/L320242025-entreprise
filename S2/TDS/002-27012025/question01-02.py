employes_origine = [
    "Patrick",
    "Marie",
    "Jean",
    "Julie",
    "Patrick",
    "Sophie",
    "Pierre",
    "Paul",
    "Julie",
    "Jacques",
    "Patrick",
    "François",
    "Luc",
    "Julie",
]
liste_employe = ["Patrick", "Pierre", "Julie"]


def remove_employe(employes_origine, liste_employe):
    liste_tempo = employes_origine.copy()
    for employe in liste_employe:
        while employe in liste_tempo:
            liste_tempo.remove(employe)
    return liste_tempo

print(employes_origine)
print(liste_employe)
print(remove_employe(employes_origine, liste_employe))
print(employes_origine)