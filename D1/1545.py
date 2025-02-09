# 거꾸로 출력해 보아요

a = int(input())
b = a
k = []

while a >= 0:
    k.append(a)
    a = a-1

while a <= b:
    print(k[a], end = ' ')

# for i in k:
#     print(i, end = " ")