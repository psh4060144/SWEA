# 사칙연산

T = 10  # test case 는 10으로 고정
for tc in range(1, T + 1):  # test case 만큼 반복

    N = int(input())  # node 갯수 입력

    left = [0] * (N + 1)  # 좌측 자식과의 연결을 확인하기 위해 list 제작.
    right = [0] * (N + 1)  # 우측 자식과의 연결을 확인하기 위해 list 제작.
    node_symbol = [None] * (N + 1)  # node 번호와 해당하는 글자를 받기 위해 list 제작.

    for i in range(1, N + 1):  # node 갯수만큼 반복. 0번 node 는 없기 때문에 1부터 시작.
        node, symbol, *edge = input().split()  # node 번호, symbol(기호 or 숫자), 연결 정보를 받음.

        if symbol.isdecimal():  # symbol 이 기호인지 숫자인지 판별
            node_symbol[i] = [int(node), int(symbol)]  # 숫자라면 int 로 만들어줌.
        else:
            node_symbol[i] = [int(node), symbol]  # 기호라면 그대로 넣음.

        if edge:  # 연결이 되어 있다면
            if len(edge) == 2:  # 2개 연결되어 있다면
                left[i] = int(edge[0])  # 좌측 자식은 left 에,
                right[i] = int(edge[1])  # 우측 자식은 right 에 입력
            else:  # 1개라면
                left[i] = int(edge[0])  # left 에 그냥 입력.


    def postorder(v):  # 후위 순회 함수
        if left[v] or right[v]:  # 자식 node 가 있다면
            a = postorder(left[v])
            b = postorder(right[v])  # 그 자식 node 의 return 값을 각각 저장

            if node_symbol[v][1] == '+':  # node 본인이 사칙연산이라면 각각 계산하여 return
                return a + b
            elif node_symbol[v][1] == '-':
                return a - b
            elif node_symbol[v][1] == '*':
                return a * b
            else:
                return a / b

        return node_symbol[v][1]  # node 본인이 숫자라면 그 숫자를 return.

    print(f'#{tc} {int(postorder(1))}')  # 마지막 숫자를 정수화하여 양식에 맞게 출력.