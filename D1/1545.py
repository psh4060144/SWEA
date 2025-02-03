# 거꾸로 출력해 보아요

a = int(input())
k = []

while a >= 0:
    k.append(a)
    a = a-1

for i in k:
    print(i, end = " ")