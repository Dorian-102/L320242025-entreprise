liste = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

diviseurs = {num:[x for x in range(1, num+1) if num % x == 0] for num in liste}

print(diviseurs)