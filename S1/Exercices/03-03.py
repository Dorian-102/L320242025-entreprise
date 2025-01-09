ma_liste = ["T", "O", "A", "p", "t", "p",
            "l", "o", "e", "s", "t", "t",
            "r", "s", "t", "t", "t", "u", 
            "m", "m", "p"]

nouvelle_liste = []

for index, lettre in enumerate(ma_liste):
    if index % 2 != 0:
        nouvelle_liste.append(lettre)

ma_liste = nouvelle_liste

print(ma_liste)

while 't' in ma_liste:
    ma_liste.remove('t')

print(ma_liste)
