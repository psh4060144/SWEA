# 몫과 나머지 출력하기

linetotal = int(input())
inputdata = list(input() for _ in range(linetotal))
x = 0

for i in inputdata:
    a = list(map(int, i.split()))
    print(f'#{x+1} {a[0] // a[1]} {a[0] % a[1]}')
    x += 1