def separe(nombres):
    impairs = []
    pairs = []
    for nombre in nombres:
        if nombre % 2 == 0:
            pairs.append(nombre)
        else:
            impairs.append(nombre)
    return tuple(pairs), tuple(impairs)

print(separe((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
