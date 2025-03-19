# 이진 탐색

def binary_search(start, end, key, direction):
    # 시작 index, 끝 index, 찾는 값, 진행 방향. 1 = 오른쪽, 2 = 왼쪽, 0 = 시작으로 표시.
    if start > end:  # 범위가 역전되거나, 비교 가능한 요소가 없다.
        return 0

    mid = (start + end) // 2

    if key == A[mid]:  # 찾았다면
        return 1
    elif key > A[mid] and direction != 1:  # 찾는 값이 중간값보다 더 크다면 큰 부분만 보면 됨.
        return binary_search(mid + 1, end, key, 1)
    elif key < A[mid] and direction != 2:  # 찾는 값이 중간값보다 더 작다면 작은 부분만 보면 됨.
        return binary_search(start, mid - 1, key, 2)

    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(M):
        if binary_search(0, N - 1, B[i], 3):
            cnt += 1
    print(f'#{tc} {cnt}')

