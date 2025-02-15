# 농작물 수확하기

T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    N = int(input())  # 농장의 크기를 받음
    n = N // 2 + 1  # 농장 중간의 행 번호를 설정.
    harvest = 0  # 총 수확량을 설정
    mdl_sum = 0  # 중간 행 수확량을 설정

    farm = [list(map(int, input())) for _ in range(N)]  # 전체 농장을 받음

    for i in range(n):  # 농장 중간 바로 위 행까지 실행
        for j in range(n - i - 1, n + i):  # 중간 열에서 좌우로 1칸씩 늘려가며 수확
            harvest += farm[i][j]  # 수확해서 총 수확량에 저장
            harvest += farm[N - i - 1][j]  # 밑에서부터 올라오면서도 진행

    for k in range(N):  # 중간 행 수확
        harvest -= farm[n - 1][k]  # 중간 행을 두 번 수확했으므로 겹치는 양을 빼줌.

    print(f'#{tc} {harvest}')
