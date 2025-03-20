# 최소 비용

delta = [(0, 1), (1, 0)]  # 우, 하 delta. 좌, 상으로 움직이면 당연히

T = int(input())
for tc in range(1, T + 1):

    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]

