# 탈주범 검거

# 파이프의 생김새를 dictionary 형태로 저장.
pipe = { # 상      우      하      좌
    1: [(-1, 0), (0, 1), (1, 0), (0, -1)],
    2: [(-1, 0), (0, 0), (1, 0), (0, 0) ],
    3: [(0, 0) , (0, 1), (0, 0), (0, -1)],
    4: [(-1, 0), (0, 1), (0, 0), (0, 0) ],
    5: [(0, 0) , (0, 1), (1, 0), (0, 0) ],
    6: [(0, 0) , (0, 0), (1, 0), (0, -1)],
    7: [(-1, 0), (0, 0), (0, 0), (0, -1)],
    9: [(1, 2, 5, 6), (1, 3, 6, 7), (1, 2, 4, 7), (1, 3, 4, 5)],  # 상, 우, 하, 좌에서 유효한 파이프.
}


def solve(R, C, L):  # 파이프를 순회하며 이동할 수 있는 칸을 세는 함수.
    queue = [(R, C, 1)]  # (맨홀의 세로 위치, 맨홀의 가로 위치, 이동 거리)를 순차적으로 입력.
    visited = [[0] * M for _ in range(N)]  # 방문 표시를 위해 2차원 list 를 만듦.
    visited[R][C] = 1  # 현재 위치에 방문 표시.
    count = 1  # 이동할 수 있는 칸을 변수로 설정하고, 현재 위치를 미리 추가.

    while queue:  # queue 가 없어질 때까지 반복.
        current = queue.pop(0)  # 현재 위치를 current 에 저장.
        if current[2] == L:  # 최대 이동 거리에 도달했다면
            break  # 즉시 종료.
        key = field[current[0]][current[1]]  # 현재 위치의 파이프 모양을 저장.
        for i in range(4):  # 현재 위치의 상, 우, 하, 좌의 파이프를 돌아가면서 확인하는데
            r = current[0] + pipe[key][i][0]
            c = current[1] + pipe[key][i][1]  # 각 위치를 새로 좌표화.
            if 0 <= r < N and 0 <= c < M and not visited[r][c] and field[r][c] in pipe[9][i] :  # 범위 안이고, 방문한 적 없으며, 유효한 파이프라면
                queue.append((r, c, current[2] + 1))  # 이동 거리에 1을 추가한 해당 위치를 queue 에 저장.
                visited[r][c] = 1  # 해당 위치에 방문 표시.
                count += 1  # 이동할 수 있는 칸을 추가.

    return count  # 순회가 끝났다면 이동할 수 있는 칸을 반환.


T = int(input())  # test case
for tc in range(1, T + 1):  # test case 만큼 반복.

    N, M, R, C, L = map(int, input().split())  # 세로 길이 N, 가로 길이 M, 맨홀의 세로 위치 R, 맨홀의 가로 위치 C, 소요 시간 L
    field = [list(map(int, input().split())) for _ in range(N)]  # 지도를 입력.
    result = solve(R, C, L)  # 이동할 수 있는 칸을 세는 함수 실행.
    print(f'#{tc} {result}')  # 양식에 맞게 출력.