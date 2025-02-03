# 중간값 찾기

a = int(input())
b = list(map(int,input().split()))
print(a)
print(b)

b.sort()
print(b)
print(type(b))
print(b[int((a - 1) / 2)])
print(type(b[int((a - 1) / 2)]))