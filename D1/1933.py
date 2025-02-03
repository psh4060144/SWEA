# 간단한 n의 약수

n = int(input())
x = 1
a = []

while x < n/2:
    if n % x == 0:
        a.extend([x, int(n/x)])
    else:
        pass
    x += 1

a = list(set(a))
a.sort()

for i in a:
    print(i, end = " ")