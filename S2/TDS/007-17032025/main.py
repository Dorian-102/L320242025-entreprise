from data import MESSAGE, pays
from fct import cherche_ville

while True:
    ville = input(MESSAGE)
    if ville == "":
        break
    print(cherche_ville(ville, pays))
    
