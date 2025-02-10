from functools import reduce
numbers = [1, 3, 10, 45, 6, 50]

def is_even(x):
    return x % 2 == 0

def somme(a, b):
    return a + b

even_numbers = filter(is_even, numbers)
print(even_numbers)
#print(list(even_numbers)) attention vide l'itérateur
print(reduce(somme, even_numbers))
print(reduce(somme, filter(is_even, numbers)))
