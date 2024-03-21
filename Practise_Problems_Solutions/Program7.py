output = []
for i in range(1000, 3001):
    if all(int(value) % 2 == 0 for value in str(i)):
        output.append(str(i))
print(','.join(output))
