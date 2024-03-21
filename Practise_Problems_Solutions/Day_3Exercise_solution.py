lst = [x for x in range(1200, 2001, 130)]
lst_add = [x + 6 for x in lst]
squarelst = [x**2 for x in lst]
squaresgreater = [x**2 for x in lst if x**2 > 50]
vehicles_dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
vehicles_below = [key.upper() for key, value in vehicles_dict.items() if value < 5000]

print(lst)
print(lst_add)
print(squarelst)
print(squaresgreater)
print(vehicles_below)
