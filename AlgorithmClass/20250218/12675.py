T = int(input())  # tc

for tc in range(1, T + 1):  # tc 만큼 반복

    N = int(input())  # 배열의 변의 길이를 입력

    matrix = [list(map(int, input().split())) for _ in range(N)]  # 배열을 입력

    col = [0] * N  # 열이 겹치지 않는 값만 사용하기 위해(사용한 열을 표시하기 위해) list 를 제작
    sum_min = 101  # 합의 최댓값이 100이므로 그것보다 크게 잡아서 최솟값을 입력할 수 있게 해 줌

    def solve(i, sum):  # 최솟값을 찾아 바꿔주는 함수
        global sum_min  # 매 함수마다 바뀐 sum_min 값을 사용해주기 위해 global 변수로 설정

        if sum > sum_min:  # backtracking
            return

        if i > N - 1:  # 모든 행을 봤다면
            if sum < sum_min:
                sum_min = sum  # sum_min 값을 작은 값으로 변경
                return

        for j in range(N):  # 모든 열을 보면서
            if col[j] == 0:  # 사용하지 않은 열일 때
                col[j] = 1  # 사용 표시를 하고
                solve(i + 1, sum + matrix[i][j])  # 다음 행에서 다시 열을 참조. 또, sum 값에 해당 숫자를 더해 넘겨줌
                col[j] = 0  # 사용 표시 해제

    solve(0, 0)  # 함수 실행
    print(f'#{tc} {sum_min}')  # 양식에 맞게 출력