# 전봇대

T = int(input())
for tc in range(1, T + 1):

    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    # for i in range(N):
    #     for j in range(N):
    #         if lines[i][0] < lines[j][0] and lines[i][1] > lines[j][1]:
    #             cnt += 1

    lines.sort(key=lambda x: x[0])
    for i in range(N):
        for j in range(i + 1, N):
            if lines[i][1] > lines[j][1]:
                cnt += 1

    print(lines)
    print(f'#{tc} {cnt}')
