T = int(input())  # test case
for tc in range(1, T + 1):  # test case 만큼 반복

    N, M, L = map(int, input().split())  # node 의 갯수 N, leaf node 의 갯수 M, 출력용 node L 를 입력.
    tree = [0] * (N + 1)  # 자식 node 의 값을 합산하기 위해 기본 tree 구조 설정.

    for i in range(M):  # 모든 leaf node 를 tree 에 입력
        a, b = map(int, input().split())
        tree[a] = b

    for j in range(N, L+1, -1):  # 지정 node 의 값을 출력하면 되므로 지정 node 까지만 반복해주면 됨.
        tree[j // 2] += tree[j]  # leaf node 의 값을 부모 node 에 더해주는 과정을 반복.

    print(f'#{tc} {tree[L]}')  # 양식에 맞게 출력.