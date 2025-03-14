N = int(input())
n = [0] * (N + 1)
for i in range(1, N + 1):
    n[i] = int(input())

if N == 1:
    print(n[1])
elif N == 2:
    print(n[1] + n[2])
else:
    dp = [0] * (N + 1)
    dp[1] = n[1]
    dp[2] = n[1] + n[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i - 3] + n[i - 1] + n[i], dp[i - 2] + n[i])

    print(dp[N])
