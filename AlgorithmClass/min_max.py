# min max

T = int(input())

for i in range(1, T+1):

    N = int(input())
    arr = list(map(int, input().split()))
    max_idx = 0
    min_idx = 0

    for j in range(N):
        if arr[max_idx] < arr[j]:
            max_idx = j
        if arr[min_idx] > arr[j]:
            min_idx = j

    print(f'#{i} {arr[max_idx] - arr[min_idx]}')