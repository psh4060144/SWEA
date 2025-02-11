# 회문

T = int(input())  # test case

for i in range(1, T + 1):  # test case 만큼 반복

    N, M = list(map(int, input().split()))  # 한 줄의 글자 갯수, 원하는 글자 갯수를 나눠 받는다.

    field = [list(input()) for _ in range(N)]  # 모든 글자를 받는다

    for row in range(N):  # 행 판별
        for col_start in range(N - M + 1):  # M이 N보다 작을 수 있으므로 탐색이 가능하도록 앞의 몇 개만 탐색한다
            new_line = []
            reversed_new_line = []  # 정방향 list, 역방향 list 를 만든다.

            for col in range(M):  # 요소를 하나씩 넘겨가면서
                new_line.append(field[row][col_start + col])  # 앞의 요소는 정방향 list 에,
                reversed_new_line.append(field[row][col_start + (M - col - 1)])  # 뒤의 요소는 역방향 list 에 각각 append.

        if new_line == reversed_new_line:  # 정방향 list 와 역방향 list 를 비교해서 같으면 출력하고 break.
            print(f'#{i} {"".join(new_line)}')
            break

    for row in range(N):  # 열 판별. 로직은 위와 완벽하게 동일.
        for col_start in range(N - M + 1):
            new_line = []
            reversed_new_line = []

            for col in range(M):
                new_line.append(field[col_start + col][row])
                reversed_new_line.append(field[col_start + (M - col - 1)][row])

        if new_line == reversed_new_line:
            print(f'#{i} {"".join(new_line)}')
            break
