a = [1, 2, 3]
b = [4, 5, 6]

for i in range(len(b)):
    a.append(b[i])
b[2] = 9
print(a)