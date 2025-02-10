numbers = [1, 3, 10, 45, 6, 50]

def is_even(x):
    return x % 2 == 0

def square(x):
    return x * x
#    return x ** 2

even_numbers = filter(is_even, numbers)
print(even_numbers)
#print(list(even_numbers)) attention vide l'itérateur
print(list(map(square, even_numbers)))
print(list(map(square, filter(is_even, numbers))))


