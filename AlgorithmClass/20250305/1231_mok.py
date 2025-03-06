# 중위순회하면서 출력
def solve(v):
    if v is None:  # 없는 노드라면
        return

    left = tree[v][0]  # 좌측 자식 노드
    right = tree[v][1]  # 우측 자식 노드
    value = tree[v][2]  # value
    solve(left)
    print(value, end='')
    solve(right)


# 중위순회하면서 반환해서 한번에 전체 출력
def solve2(v):
    if v is None:
        return ''  # return 값이 None + str + None 이 되지 않기 위해 빈 str 을 반환.

    left = tree[v][0]  # 좌측 자식 노드
    right = tree[v][1]  # 우측 자식 노드
    value = tree[v][2]  # value
    left_value = solve2(left)
    right_value = solve2(right)
    return left_value + value + right_value


T = 10
for tc in range(1, T + 1):
    N = int(input())  # 정점 갯수 N 입력
    tree = [[None, None, None] for _ in range(N + 1)]  # 정점이 1부터 시작하므로 N + 1개를 만들어야 함. 왼쪽 자식, 오른쪽 자식, value 의 순서.
    for _ in range(N):  # N 개의 정점 정보를 각각 받음
        node = input().split()
        # node[0] = 현재 정점 정보(str)
        # node[1] = 정점 value(str)
        # (있다면) node[2] = 왼쪽 자식 번호(str), (있다면) node[3] = 오른쪽 자식 번호(str)
        num = int(node[0])
        tree[num][2] = node[1]
        if len(node) >= 3:
            tree[num][0] = int(node[2])
        if len(node) >= 4:
            tree[num][1] = int(node[3])

    # print(f'#{tc}', end=' ')
    # solve(1)
    # print()

    result = solve2(1)
    print(f'#{tc} {result}')