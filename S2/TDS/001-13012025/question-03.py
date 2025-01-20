from random import randint

print("Bienvenue dans le jeu de devinette de nombres!")

while True:
    nombre = randint(1, 100)
    essais = 0
    while True:
        essais += 1
        devinette = int(input("Veuillez saisir une valeuir (1..100) : "))
        if devinette < nombre:
            print("La valeur à trouver est plus grande")
        elif devinette > nombre:
            print("La valeur à trouver est plus petite")
        else:
            print(f"Gagné en {essais} coup(s).")
            break
    print("Voulez-vous rejouer? (o/n)")
    rejouer = input()
    if rejouer != 'o':
        break