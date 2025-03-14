# 부분 수열의 합


def subset(tar):  # 부분집합 하나를 구해, 합을 비교하는 함수.
    sum_v = 0  # 합을 구하기 위해 변수를 설정.

    for i in range(N):  # 숫자 갯수만큼 반복.

        if tar & 0x1:  # 입력한 숫자와 1을 비교해서
            sum_v += A[i]  # 1이 있으면 있는 자리의 숫자를 변수에 합산.
        if sum_v > K:  # 반복을 덜 돌았는데 이미 목표값보다 크다면
            return 0  # 바로 0을 반환 후 종료.
        tar >>= 1  # 입력한 숫자를 2로 나눠 줌.

    if sum_v == K:  # 목표값과 일치하면
        return 1  # 해당 부분집합은 유효하므로 1을 반환 후 종료.

    return 0  # 반복을 다 돌아도 목표값보다 작다면 0을 반환 후 종료.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N, K = map(int, input().split())  # 자연수 갯수 N, 목표값 K 입력.
    A = list(map(int, input().split()))  # 수열 입력.
    count = 0  # 부분 수열의 합이 목표값과 같아지는 경우의 수를 세기 위해 변수를 설정.

    for tar in range(1, 1 << N):  # 모든 부분집합을 반복해서
        count += subset(tar)  # 유효한 부분집합의 갯수를 셈.

    print(f'#{tc} {count}')  # 양식에 맞게 출력.
