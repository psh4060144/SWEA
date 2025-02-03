# 아주 간단한 계산기

a = list(map(int,input().split()))

def fourcals(a):
    k = [a[0] + a[1], a[0] - a[1], a[0] * a[1], a[0] // a[1]]
    return k

for i in fourcals(a):
    print(i)