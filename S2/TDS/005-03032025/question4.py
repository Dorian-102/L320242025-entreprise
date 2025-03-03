liste_chaine = ['pomme', 'banane', 'poire']

liste = [''.join(['*' if char.lower() in 'aeiou' else char for char in mot]) for mot in liste_chaine]

print(liste)