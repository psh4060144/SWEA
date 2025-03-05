# subtree

T = int(input())  # test case
for tc in range(1, T + 1):  # test case 만큼 반복

    E, N = map(int, input().split())  # 간선의 갯수, subtree 의 root node 번호 입력.
    edge = list(map(int, input().split()))  # 간선 정보 입력
    left = [0] * 1002  # 왼쪽 자식을 입력하기 위해 list 제작.
    right = [0] * 1002  # 오른쪽 자식을 입력하기 위해 list 제작.
    count = 0  # subtree 의 node 갯수를 세기 위해 변수 설정.

    for i in range(0, E * 2, 2):  # 간선 정보를 통해 left 와 right 에 정보를 입력
        if not left[edge[i]]:  # 좌측부터 입력하는데, 0이라면(값이 입력되어 있지 않다면)
            left[edge[i]] = edge[i + 1]  # 좌측에 자식 node 번호 입력.
        else:  # 값이 입력되어 있다면
            right[edge[i]] = edge[i + 1]  # 우측에 자식 node 번호 입력.


    def preorder(v):  # 전위 순회 함수
        global count  # 전위 순회 하면서 count 값을 바꿔 줌.
        if v:  # 존재하는 node 라면
            count += 1  # count 에 1을 더해주고
            preorder(left[v])
            preorder(right[v])  # 자식 node 검사.


    preorder(N)  # 함수 실행
    print(f'#{tc} {count}')  # 양식에 맞게 출력