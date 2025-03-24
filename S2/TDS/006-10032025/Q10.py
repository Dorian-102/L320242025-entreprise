liste = ['apple', 'banana', 'tttt', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'imbe', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'dddd', 'strawberry', 'tangerine', 'ugli', 'vanilla', 'kkkk', 'ximenia', 'yuzu', 'zucchini']

nombre_voyelles = {fruit:sum([1 for lettre in fruit if lettre in 'aeiou']) for fruit in liste}

dict = {}
For fruit in liste:
    listvoy= []
    for lettre in fruit:
        if lettre in 'aeiou':
            listvoy.append(1)
    dict[fruit] = sum(listvoy)

nombre_voyelles2  = {fruit:sum([1 for lettre in fruit if lettre in 'aeiou']) for fruit in liste if any(lettre.lower() in 'aeiou' for lettre in fruit)}

liste2 = [[lettre.lower() in 'aeiou'   for lettre in fruit] for fruit in liste]
print(liste2)   

print(nombre_voyelles)
print(nombre_voyelles2)