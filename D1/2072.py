# 홀수만 더하기

linetotal = int(input())
inputdata = list(input() for _ in range(linetotal))
x = 0

for _ in inputdata:
    a = inputdata[x]
    a = list(map(int, a.split()))
    for i in a:
        if i % 2 == 0:
            a[a.index(i)] = 0
    print('#{} {}'.format(x+1, sum(a)))
    x += 1