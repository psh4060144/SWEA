# 스위치 조작

T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    N = int(input())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))  # 들어오는 정보를 받음
    count = 0  # 스위치를 누르는 횟수를 세기 위해 변수를 설정.

    for i in range(N):  # 모든 전등을 지나가면서 비교하는데,
        if Ai[i] != Bj[i]:  # 다른 전등을 만난다면
            for j in range(i, N):  # 그 뒤의 모든 전등의 상태를 변경한다.
                if Ai[j] == 0:
                    Ai[j] = 1
                else:
                    Ai[j] = 0
            count += 1  # 그리고 스위치 누른 횟수에 1을 더한다.

    print(f'#{tc} {count}')