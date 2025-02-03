# 최대수 구하기

linetotal = int(input())
inputdata = list(input() for _ in range(linetotal))
x = 0

for _ in inputdata:
    a = inputdata[x]
    a = list(map(int, a.split()))
    a.sort()
    print(f'#{x+1} {a.pop()}')
    x += 1