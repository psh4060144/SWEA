# 베이비진 게임


def check(arr):  # finding run or triplet
    for i in range(10):
        if arr[i] >= 3:
            return True
        elif arr[i] >= 1:
            if i < 8 and arr[i + 1] >= 1 and arr[i + 2] >= 1:
                return True
    return False


def solve():  # disposing cards
    for i in range(12):
        if i % 2:
            p2[cards[i]] += 1
            if check(p2):
                return 2
        else:
            p1[cards[i]] += 1
            if check(p1):
                return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    result = solve()
    print(f'#{tc} {result}')
