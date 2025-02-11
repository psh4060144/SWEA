# T = int(input())

# for i in (1, T + 1):
    
N = int(input())

field = [[0] * N for _ in range(N)]
el = 1

for row in range(N):
    for col in range(N):
        field[row][col] += el
        el += 1

a = field[]