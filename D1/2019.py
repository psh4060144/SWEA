# 더블더블

a = int(input())
x = 0
k = []

while x < a+1:
    k.append(2**x)
    x += 1

for i in k:
    print(i, end = " ")