# 최소 생산 비용


def solve(i, sum):  # 최솟값을 구하는 함수.
    global sum_min  # 최솟값을 구하기 위해 전역 변수를 설정.
    global col  # 확인한 행을 표시하기 위해 전역 변수를 설정.

    if sum_min < sum:  # pruning. sum 값이 이미 sum_min 보다 크다면 답이 될 수 없으므로 조기 종료.
        return

    if i > N - 1:  # 모든 행을 봤다면
        if sum < sum_min:  # 최솟값과 비교하여
            sum_min = sum  # sum_min 값을 작은 값으로 변경
            return

    for j in range(N):  # 모든 행을 돌면서 확인.
        if col[j] == 0:  # 방문한 적 없는 행이라면
            col[j] = 1  # 행 방문 표시를 하고
            solve(i + 1, sum + V[i][j])  # 다음 열에서 재귀 호출.
            col[j] = 0  # 재귀가 끝나면 방문한 행을 다시 0으로 바꿔 줌.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복

    N = int(input())  # 제품 수 N 을 입력.
    V = [list(map(int, input().split())) for _ in range(N)]  # 공장 별 생산 비용을 입력.

    col = [0] * N  # 행 방문 표시를 위해 제품 수 만큼의 list 제작.
    sum_min = 99 * N + 1  # 최솟값을 구하기 위해 값을 크게 만들어 줌.

    solve(0, 0)  # 최솟값을 구하는 함수 실행.

    print(f'#{tc} {sum_min}')  # 양식에 맞게 출력.
