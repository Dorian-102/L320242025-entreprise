phrase = "Le papillon est un insecte"

liste =  [len(mot) for mot in phrase.split()]

print(liste)

liste1 = ['pomme', 'banane', 'poire']

liste2= [(mot, len(mot)) for mot in liste1]

print(liste2)