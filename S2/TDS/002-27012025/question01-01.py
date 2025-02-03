employes_origine = [
    "Patrick",
    "Marie",
    "Jean",
    "Sophie",
    "Pierre",
    "Paul",
    "Jacques",
    "François",
    "Luc",
    "Julie",
]
liste_employe = ["Patrick", "Pierre", "Julie"]


def remove_employe(employes_origine, liste_employe):
    for employe in liste_employe:
        if employe in employes_origine:
            employes_origine.remove(employe)
    return employes_origine

print(employes_origine)
print(liste_employe)
print(remove_employe(employes_origine, liste_employe))