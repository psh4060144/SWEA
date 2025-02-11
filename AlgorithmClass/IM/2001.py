# 파리 퇴치

def flapper(row_start, col_start):  # 한 번에 잡을 수 있는 파리의 수를 구하는 함수
    fly_sum = 0  # return 하기 위해 변수를 설정.
    
    for row in range(M):
        for col in range(M):
            fly_sum += field[row_start + row][col_start + col]  # 파리채의 범위 내에 있는 모든 수를 더함
    
    return fly_sum

T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    N, M = list(map(int, input().split()))  # 배열 한 변의 길이, 파리채 한 변의 길이를 받음

    field = [list(map(int, input().split())) for _ in range(N)]  # 총 배열을 field 로 설정.
    sum_max = 0  # 최대 파리 수를 구하기 위해 변수를 설정.

    for row in range(N - M + 1):
        for col in range(N - M + 1):  # 파리채의 기준이 [0][0]이므로 파리채가 들어갈만큼만 반복
            sum = flapper(row, col)  # 파리의 수를 모두 더하는 것을 반복.
            
            if sum_max < sum:  # 가장 큰 수를 찾음.
                sum_max = sum

    print(f'#{tc} {sum_max}')