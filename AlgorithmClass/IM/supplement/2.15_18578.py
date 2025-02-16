# 풍선팡 보너스 게임

T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    N = int(input())  # 풍선 격자의 길이를 입력

    field = [list(map(int, input().split())) for _ in range(N)]  # 길이만큼 풍선 점수를 받음

    sum_max = 0  # 모든 풍선이 양의 정수의 점수를 가지므로, sum_max 는 0보다 크다.
    sum_min = 1000  # 각 풍선의 최대 점수가 9점을 넘지 못하고, N 또한 20을 넘지 못하기 때문에 sum_min은 1000보다 작다.

    for i in range(N):
        for j in range(N):  # 하나의 풍선을 기준으로 잡아
            sum = 0  # 그 기준의 가로 세로 합을 구하기 위해 변수를 설정
            
            for k in range(N):  # 기준의 행과 열의 점수를 모두 합산
                sum += field[i][k] + field[k][j]
                
            sum -= field[i][j]  # 기준값이 두 번 들어가므로 한 번 빼 줌.
            
            if sum_max < sum:
                sum_max = sum
            if sum_min > sum:
                sum_min = sum  # sum_max 와 sum_min 을 산출.

    print(f'#{tc} {sum_max - sum_min}')