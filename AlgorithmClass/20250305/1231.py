# 중위순회

T = 10  # test case 는 10으로 고정
for tc in range(1, T + 1):  # test case 만큼 반복

    N = int(input())  # 글자 갯수 입력
    left = [0] * (N + 1)  # 좌측 자식과의 연결을 확인하기 위해 list 제작.
    right = [0] * (N + 1)  # 우측 자식과의 연결을 확인하기 위해 list 제작.
    node_letter = [None] * (N + 1)  # node 번호와 해당하는 글자를 받기 위해 list 제작.

    for i in range(1, N + 1):  # node, 글자, 연결 정보를 받아오는데
        (node, letter, *edge) = input().split()  # node, 글자, 연결 정보를 각각 나눠서 받음
        node_letter[i] = [int(node), letter]  # node 와 글자는 node_letter 에 정리. node 는 숫자이므로 int 를 취해 줌.

        if edge:  # 다른 node 와 연결되어 있는 node 라면
            if len(edge) == 2:  # 2개 연결된 경우
                if edge[0] > edge[1]:  # 연결된 node 를 보아
                    edge[0], edge[1] = edge[1], edge[0]  # 둘 중 작은 node 를 왼쪽에 배치
                left[i] = int(edge[0])
                right[i] = int(edge[1])  # 이후 왼쪽 node 를 left 에, 오른쪽 node 를 right 에 삽입.
            else:  # 1개 연결된 경우
                left[i] = int(edge[0])  # node 를 left 에 삽입.


    def inorder(v):  # 중위 순회 함수
        if node_letter[v]:  # node 가 존재한다면
            inorder(left[v])  # 왼쪽으로 들어가고
            print(node_letter[v][1], end='')  # 해당 노드의 글자를 print 한 후
            inorder(right[v])  # 이후 오른쪽으로 들어감

    print(f'#{tc}', end=' ')  # 양식에 맞게 출력
    inorder(1)  # 함수 실행하여 양식에 맞게 출력
    print()  # 줄바꿈