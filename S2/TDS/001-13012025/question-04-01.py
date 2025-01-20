netamout = 0
while True:
    s = input()
    if not s:
        break
    values = s.split()
    if len(values) != 2:
        print("Invalid input")
        continue
    operation = values[0].upper()
    somme = int(values[1])
    if operation == 'D':
        netamout += int(somme)
    elif operation == 'R':
        netamout -= int(somme)
    else:
        print("Invalid input")

print(netamout)