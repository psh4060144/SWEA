# 수영장


# DP - Bottom-Up
T = int(input())
for tc in range(1, T + 1):

    d, m, m3, y = map(int,input().split())
    plan = [0] + list(map(int, input().split()))

    dp = [0] * 13
    dp[1] = min(plan[1] * d, m)






    # 3월 ~ 12월은 반복하며 계산
    for month in range(3, 13):
        # N 월의 최소 비용 후보
        # 1. N - 3월에 3개월 이용권을 구입한 경우
        # 2. N - 1월의 최소 비용 + 1일권 구매
        # 3. N - 1월의 최소 비용 + 1달권 구매
        dp[month] = min(
            dp[month - 3] + m3,
            dp[month - 1] + (plan[month] * d),
            dp[month - 1] + m,
        )

    # 12월의 누적 최소 금액 vs 1년권
    print(f'#{tc} {min(dp[12], y)}')


# 일반적인 문제의 접근 방식

# 1. Top-Down 방식
# - DP(Memoization)
# - 거듭제곱 문제

# 2. Bottom-Up 방식
# - 시작점을 정해둔다.
# - 앞으로 쌓아 나아가면서 진행.
#    - 기존값을 활용.
#    - 정답을 계산해서 저장하면서 진행.
#    -> 점화식을 구하는 경우가 많다.