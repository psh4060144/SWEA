# tree 를 후위순회 하면서 반환 받아 연산
def solve(v):  # v 에 연산자가 들어갈 수도 있고, 피연산자가 들어갈 수도 있다.
    if v is None:
        return

    node_value = tree[v][2]
    left = tree[v][0]
    right = tree[v][1]
    solve(left)
    solve(right)

    if node_value in '+-*/':
        if node_value == '+':
            tree[v][2] = tree[left][2] + tree[right][2]
        elif node_value == '-':
            tree[v][2] = tree[left][2] - tree[right][2]
        elif node_value == '*':
            tree[v][2] = tree[left][2] * tree[right][2]
        else:
            tree[v][2] = tree[left][2] / tree[right][2]

    else:
        tree[v][2] = int(tree[v][2])


def solve2(v):  # v 에 연산자가 들어갈 수도 있고, 피연산자가 들어갈 수도 있다.

    node_value = tree[v][2]
    if node_value.isdigit():
        return int(node_value)

    left = tree[v][0]
    right = tree[v][1]
    left_num = solve2(left)
    right_num = solve2(right)

    if node_value == '+':
        return left_num + right_num
    elif node_value == '-':
        return left_num - right_num
    elif node_value == '*':
        return left_num * right_num
    else:
        return left_num / right_num


T = 10
for tc in range(1, T + 1):
    N = int(input())  # 정점 갯수 N 입력
    tree = [[None, None, None] for _ in range(N + 1)]  # 정점이 1부터 시작하므로 N + 1개를 만들어야 함. 왼쪽 자식, 오른쪽 자식, value 의 순서.
    for _ in range(N):  # N 개의 정점 정보를 각각 받음
        node = input().split()
        num = int(node[0])
        tree[num][2] = node[1]  # 피연산자, 연산자는 문자열로 저장함에 주의.
        if len(node) == 4:
            tree[num][0] = int(node[2])
            tree[num][1] = int(node[3])

    # solve(1)
    # print(f'#{tc} {int(tree[1][2])}')

    result = solve2(1)
    print(f'#{tc} {int(result)}')