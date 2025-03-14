# 수영장

T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복

    d, m, m3, y = map(int, input().split())  # 일 요금, 월 요금, 분기 요금, 연 요금을 입력.
    plan = [0] + list(map(int, input().split()))  # 수영 계획을 입력. 앞에 0을 더해서 indexing 이 편하게 해 줌.

    dp = [0] * 13  # DP 방식으로 풀기 위해 빈 list 를 설정.
    dp[1] = min(plan[1] * d, m)  # 첫 번째 달의 최솟값을 계산. 일 요금 계산 vs 월 요금 계산
    dp[2] = min(dp[1] + plan[2] * d, dp[1] + m)  # 두 번째 달의 최솟값을 계산. 일 요금 계산 vs 월 요금 계산.

    for i in range(3, 13):  # 세 번째 달부터는 일괄적으로 수식을 적용 가능하기 때문에 반복문으로 진행.
        dp[i] = min(dp[i - 1] + plan[i] * d,  # 일 요금 계산.
                    dp[i - 1] + m,  # 월 요금 계산.
                    dp[i - 3] + m3)  # 분기 요금 계산. 3월부터 1, 2월에 분기 요금을 적용 가능하기 때문에 여기서 실행.

    print(f'#{tc} {min(dp[12], y)}')  # 연 요금까지 비교해서 양식에 맞게 출력.
