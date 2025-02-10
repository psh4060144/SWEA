T = 10

for i in range(T):

    N = int(input())

    ladder = [list(map(int, input().split())) for _ in range(100)]
    last_row = 99
    arrive_idx = 0

    for col in ladder[last_row]:
        if col != 2:
            arrive_idx += 1
        else:
            break

    while last_row != 0:
            # 단축 평가
        while (arrive_idx == 0 or ladder[last_row][arrive_idx - 1] != 1)  \
                and (arrive_idx == 99 or ladder[last_row][arrive_idx + 1] != 1):
            if last_row == 0:
                break
            last_row -= 1

        if arrive_idx != 0 and ladder[last_row][arrive_idx - 1] == 1:
            while ladder[last_row][arrive_idx - 1] != 0:
                arrive_idx -= 1
            last_row -= 1

        if arrive_idx != 99 and ladder[last_row][arrive_idx + 1] == 1:
            while ladder[last_row][arrive_idx + 1] != 0:
                arrive_idx += 1
            last_row -= 1

    print(f'#{N} {arrive_idx}')