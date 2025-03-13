# 격자판의 숫자 이어 붙이기

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌 시계방향 delta.


def moving(row, col, count):
    global fulllst
    queue = [(row, col, count)]
    lst = []

    while queue:
        cr, cc, cnt = queue.pop(0)


        if cnt == 7:
            if

            continue
        for i in range(4):
            nr = cr + delta[i][0]
            nc = cc + delta[i][0]
            if 0 <= nr < 4 and 0 <= nc < 4:
                queue.append((nr, nc, cnt + 1))





# T = int(input())
# for tc in range(1, T + 1):

field = [list(map(int, input().split())) for _ in range(4)]
fulllst = []