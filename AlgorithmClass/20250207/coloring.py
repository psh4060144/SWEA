# 색칠하기

T = int(input())  # 총 test case 갯수

for i in range(1, T + 1):

    N = int(input())  # 사각형으로 색칠하는 횟수
    field = [[0] * 10 for _ in range(10)]  # 0으로 이루어진 10 * 10의 종이를 생성
    sum = 0  # 보라색의 갯수를 세기 위해 변수를 설정.

    for j in range(N):  # 매 횟수마다

        '''
        1 2 3 3 1
        3 6 6 8 1
        2 3 5 6 2
        '''

        r1, c1, r2, c2, color = list(map(int, input().split()))  # 색칠 정보
        # 빨간색 = 1, 파란색 = 2. 즉, 보라색 = 3. 1 + 2 = 3.

        '''  만약 왼쪽 위 모서리와 오른쪽 아래 모서리라고 주어지지 않은 경우
        if r1 > r2:
            r1, r2 = r2, r1
        if c1 > c2:
            c1, c2 = c2, c1
        '''

        for r in range(r1, r2 + 1):  # 칠해지는 행의 갯수
            for c in range(c1, c2 + 1):  # 칠해지는 열의 갯수

                if color == 1:  # 색 판별. 빨간색이라면~
                    if field[r][c] == 1:  # 빨간색이 칠해져 있다면 pass
                        pass
                    elif field[r][c] < 3:  # 칠해져 있지 않다면(비었거나 파랗다면) 색칠
                        field[r][c] += color

                else:  # 빨간색이 아니라면 무조건 파란색이다.
                    if field[r][c] == 2:  # 파란색이 칠해져 있다면 pass
                        pass
                    elif field[r][c] < 3:  # 칠해져 있지 않다면(비었거나 빨갛다면) 색칠
                        field[r][c] += color
    
    for el1 in range(10):
        for el2 in range(10):  # 10개의 행의 10개의 인수를 확인해서
            if field[el1][el2] == 3:  # 보라색이라면 sum에 1을 추가.
                sum += 1

    print(f'#{i} {sum}')