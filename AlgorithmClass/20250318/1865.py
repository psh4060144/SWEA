# 동철이의 일 분배


def solve(i, multiply):  # 최대 성공 확률을 구하는 함수.
    global col  # 확인한 행을 표시하기 위해 전역 변수를 사용.
    global result  # 최대 확률을 구하기 위해 전역 변수를 사용.

    if result >= multiply:  # 현재 확률이 최대 확률보다 작다면 해당 route 의 최대 확률은 반드시 최대 확률보다 작다.
        return  # prunning.

    if i == N:  # 모든 행을 봤다면
        if result < multiply:  # 현재 확률과 최대 확률을 비교하여
            result = multiply  # 더 큰 값을 최대 확률 값으로 설정.
            return  # 이후 종료.

    for j in range(N):  # 모든 행을 돌면서 확인.
        if col[j] == 0:  # 사용하지 않은 행인 경우
            col[j] = 1  # 사용 표시를 하고
            solve(i + 1, multiply * (probability[i][j] / 100))  # 현재 확률을 곱해준 후 다음 재귀 호출.
            col[j] = 0  # 재귀가 끝났다면 사용 표시를 지움.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N = int(input())  # N 명의 직원, N 개의 해야 할 일을 입력.
    probability = [list(map(int, input().split())) for _ in range(N)]  # 모든 확률을 입력.
    col = [0] * N  # 확인한 행을 표시하기 위해 list 를 제작.
    result = 0  # 최대 확률을 구하기 위해 변수를 설정.
    solve(0, 1)  # 최대 확률을 구하는 함수 실행.
    print(f'#{tc} {result * 100:.6f}')  # 양식에 맞게 출력.
