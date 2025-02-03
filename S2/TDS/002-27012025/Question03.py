points = {"poules": 1, "chiens": 3, "vaches": 5, "amis": 10}


def points_perdus(**fautes):
    total = 0
    for key, val in fautes.items():
        if key  in points:
            total += points[key] * val
    return total


# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def permisSup(**fautes):
    return points_perdus(**fautes) * 2


victimes = {}
# Programme principal =========================================================
victimes["poules"] = int(input("Combien de poules ?"))
victimes["chiens"] = int(input("Combien de chiens ?"))
victimes["vaches"] = int(input("Combien de vaches ?"))
victimes["amis"] = int(input("Combien d'amis ?"))

payer = permisSup(**victimes)

print(f'{"Rien à payer" if payer == 0 else f"Vous avez à payer {payer} euros"}')
