# 삼성시의 버스 노선

T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N = int(input())  # 버스 노선의 갯수를 입력.
    arr = [0] * 5001  # 모든 버스 노선을 설정해 둠.

    for _ in range(N):  # 버스 노선 갯수만큼 반복.
        start, end = map(int, input().split())  # 버스 노선을 받아서
        for i in range(start, end + 1):  # 그 버스 노선만큼의 정류장에
            arr[i] += 1  # 1을 더해줌.

    P = int(input())  # 정류장의 갯수를 입력.

    print(f'#{tc}', end=' ')  # 양식에 맞게 출력.
    for _ in range(P):
        print(arr[int(input())], end=' ')  # 모든 정류장에 대해 겹치는 버스 노선 갯수를 출력.
    print()  # 양식에 맞게 출력.
