# 최소합


def moving(downs, rights, cnt):  # 이동하면서 최소합을 찾는 함수

    for i in range(2):  # 아래로 갈 지, 오른쪽으로 갈 지 선택.

        if i == 0:  # 아래로 간다면
            if downs == N - 1:  # 아래 끝까지 갔다면
                continue  # 더 보지 않고 오른쪽으로 가는 것만 본다.
            else:  # 아래 끝까지 덜 갔다면
                moving(downs + 1, rights, cnt + field[downs + 1][rights])  # 아래로 이동.

        else:  # 오른쪽으로 간다면
            if rights == N - 1:  # 오른쪽 끝까지 갔다면
                continue  # 더 보지 않고 아래로 가는 것만 본다.
            else:  # 오른쪽 끝까지 덜 갔다면
                moving(downs, rights + 1, cnt + field[downs][rights + 1])  # 오른쪽으로 이동.

    global energy  # 최소합을 비교하는데,
    if downs + rights == 2 * (N - 1) and energy > cnt:  # 도착지점에 도착했고 현재 합이 최소합보다 작다면
        energy = cnt  # 최소합을 현재 합으로 변경.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N = int(input())  # 가로 칸의 수를 입력.
    field = [list(map(int, input().split())) for _ in range(N)]  # 숫자판을 입력.
    energy = float('inf')  # 최소합을 받을 수 있게 매우 큰 값으로 설정.

    moving(0, 0, field[0][0])  # 최소합을 찾는 함수 실행.

    print(f'#{tc} {energy}')  # 양식에 맞게 출력.
