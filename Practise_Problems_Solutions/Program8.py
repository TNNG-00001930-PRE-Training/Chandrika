str = input("Enter a sentence: ")
upper = 0
lower = 0
for i in str:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
print("UPPER CASE :", upper)
print("LOWER CASE :", lower)
