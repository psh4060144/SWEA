# 큰 놈, 작은 놈, 같은 놈

linetotal = int(input())
inputdata = list(input() for _ in range(linetotal))
x = 0

def compare(a, b):
    if a > b:
        return '>'
    elif a == b:
        return '='
    else:
        return '<'

for _ in inputdata:
    a = inputdata[x]
    a = list(map(int, a.split()))
    k = compare(a[0], a[1])
    print(f'#{x+1} {k}')
    x += 1