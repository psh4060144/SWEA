# 벽돌깨기


def subset(x):  # 모든 부분집합을 찾는 함수
    if x == N:
        newpath = [i for i in path]
        fullpath.append(newpath)
        return

    for i in range(W):
        path.append(i)
        subset(x + 1)
        path.pop()


def bfs(row, col):  # 공 하나를 떨궜을 때 벽돌이 터지는 함수
    queue = [(row, col)]

    while queue:
        cr, cc = queue.pop(0)
        value = field[cr][cc]
        field[cr][cc] = 0

        for i in range(4):
            for j in range(value):
                if 0 <= cr + (d_row[i] * j) < H and 0 <= cc + (d_col[i] * j) < W:
                    if field[cr + (d_row[i] * j)][cc + (d_col[i] * j)]:
                        queue.append((cr + (d_row[i] * j), cc + (d_col[i] * j)))


def falling():
    for i in range(W - 1, -1, -1):
        for j in range(H):
            if not field[i][j]:
                I = i - 1
                while I >= 0 and not field[I][j]:
                    I -= 1
                field[i][j] = field[I][j]
                field[I][j] = 0


d_row = [-1, 0, 1, 0]
d_col = [0, 1, 0, -1]  # 상, 우, 하, 좌 delta


# T = int(input())
# for tc in range(1, T + 1):

N, W, H = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(H)]
path = []
fullpath = []
fullcnt = W * H + 1

subset(0)

for i in range(W ** N):  # 부분집합 만큼 반복
    cnt = 0
    for j in range(N):  # 부분집합 내의 인수에 대해

        col = fullpath[i][j]
        row = 0
        while row < N and not field[row][col]:
            row += 1

        bfs(row, col)
        falling()

    for k in range(W):
        for l in range(H):
            if field[k][l]:
                cnt += 1

    if fullcnt > cnt:
        fullcnt = cnt

print(fullcnt)