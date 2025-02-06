# 구간합

T = int(input())

for i in range(1, T+1):

    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    min_sum = 1000000
    max_sum = 0

    for j in range(N-M+1):

        sum_value = 0

        for k in range(M):
            sum_value += arr[j+k]

        if min_sum > sum_value:
            min_sum = sum_value
        if max_sum < sum_value:
            max_sum = sum_value

    print(f'#{i} {max_sum - min_sum}')