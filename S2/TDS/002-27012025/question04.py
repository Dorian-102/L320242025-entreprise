from comptes import comptes

def synthese_familles(**comptes):
    familles = {}
    for compte in comptes.values():
        nom = compte["nom"]
        if nom not in familles:
            familles[nom] = 0
        familles[nom] += compte.get("epargne", 0)
    pauvre = min(familles,key=familles.get)
    riche = max(familles,key=familles.get)
    return (pauvre, familles[pauvre]), (riche, familles[riche])

print(synthese_familles(**comptes))