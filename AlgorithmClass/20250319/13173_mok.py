# 연산

def bfs():
    queue = [(N, 0)]

    while queue:
        num, cnt = queue.pop(0)
        if num == M:
            return cnt

        queue.append((num + 1, cnt + 1))
        queue.append((num - 1, cnt + 1))
        queue.append((num * 2, cnt + 1))
        queue.append((num - 10, cnt + 1))

    return -1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = bfs()
    print(f'#{tc} {result}')
