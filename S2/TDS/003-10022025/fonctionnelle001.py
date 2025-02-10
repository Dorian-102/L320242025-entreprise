from functools import reduce

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

integers = map(int, numbers)

print(integers)

total = reduce(lambda x, y: x + y, integers)

print(total)