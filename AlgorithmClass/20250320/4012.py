# 요리사

# idea
# N // 2 개의 식재료 부분집합을 구할 때, 첫 번째 식재료를 고정하고 나머지 식재료의 모든 부분집합을 구하면 중복 없이 구할 수 있다.


def origin(cnt, start):  # 부분집합을 구하는 함수.

    if cnt == N // 2:
        if path[0] == 0:
            subset.append(tuple(path))
        return

    for i in range(start, N):
        path.append(i)
        origin(cnt + 1, i + 1)
        path.pop()


def sub(cnt, start):  # 부분집합을 구하는 함수.

    if cnt == 2:
        A = field[subpath[0]][subpath[1]] + field[subpath[1]][subpath[0]]
        B = field[N - subpath[1] - 1][N - subpath[0] - 1] +
        return

    for i in range(start, N):
        subpath.append(i)
        sub(cnt + 1, i + 1)
        subpath.pop()


T = int(input())
for tc in range(1, T + 1):

    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    subset = []
    path = []
    subpath = []

    origin(0, 0)

