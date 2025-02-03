# 평균값 구하기

linetotal = int(input())
inputdata = list(input() for _ in range(linetotal))
x = 0

for _ in inputdata:
    a = inputdata[x]
    a = list(map(int, a.split()))
    k = round(sum(a) / len(a))
    print('#{} {}'.format(x+1, k))
    x += 1