def solve(v):
    global count
    # v 번 노드에 방문하면 count 를 1 증가.
    if v > 0:  # 정점 번호가 있다면
        count += 1
        solve(tree[v][0])
        solve(tree[v][1])


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[0, 0] for _ in range(E + 2)]  # E + 1 번 index 를 사용하기 위해 E + 2 개를 만듦.
    for i in range(0, E * 2, 2):
        a, b = edges[i], edges[i + 1]
        if not tree[a][0]:
            tree[a][0] = b
        else:
            tree[a][1] = b

    count = 0
    solve(N)
    print(f'#{tc} {count}')