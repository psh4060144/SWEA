# 수영장


# 완전 탐색
def recur(month, total_cost):
    global min_answer

    if month > 12:
        min_answer = min(min_answer, total_cost)
        return
    if min_answer < total_cost:
        return

    # 1일 권으로 사는 경우
    recur(month + 1, total_cost + (plan[month] * d))
    # 1달 권으로 사는 경우
    recur(month + 1, total_cost + m)
    # 3달 권으로 사는 경우
    recur(month + 3, total_cost + m3)
    # 1년 권으로 사는 경우.
    recur(month+12, total_cost + y)


T = int(input())
for tc in range(1, T + 1):

    d, m, m3, y = map(int,input().split())
    plan = [0] + list(map(int, input().split()))
    min_answer = 10000000000000000
    recur(1, 0)
    print(min_answer)