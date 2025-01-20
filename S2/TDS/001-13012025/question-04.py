netamout = 0
while True:
    s = input()
    if s:
        if s.startswith('D'):
            netamout += int(s[2:])
        elif s.startswith('R'):
            netamout -= int(s[2:])
        else:
            print("Invalid input")
    else:
        break

print(netamout)