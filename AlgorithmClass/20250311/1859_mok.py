# 백만 장자 프로젝트

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 총 일수
    data = list(map(int, input().split()))
    money = 0  # 총 수익금
    today = 0  # 현재 날짜

    while today < N:
        max_day = today  # 최고 금액 날짜
        for i in range(today, N):  # 최댓값 찾기
            if data[max_day] < data[i]:
                max_day = i

        for j in range(today, max_day):  # 수익 구하기. 최고 금액 - 그 전 날짜들의 금액
            money += data[max_day] - data[j]

        today = max_day + 1  # 현재 날짜를 최고 금액 날짜 다음 날짜로 설정.

    print(f'#{tc} {money}')
