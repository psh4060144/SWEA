# 정사각형 방

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌 delta.


def bfs(row, col):  # 이동할 수 있는 최대 칸을 세는 함수.
    queue = [(row, col, 1)]  # 행, 열, 칸 수를 입력.
    visited = [[0] * N for _ in range(N)]  # 방문 표시를 위해 빈 2차원 list 를 제작.
    visited[row][col] = 1  # 현재 위치를 방문 표시.

    while queue:  # queue 가 빌 때까지 반복.
        cr, cc, cnt = queue.pop(0)  # 현재 위치의 행, 열, 칸 수를 추출.
        current = field[cr][cc]  # 현재 위치의 값을 저장.
        for i in range(4):  # 상하좌우 4칸을 보는데,
            nr, nc = cr + delta[i][0], cc + delta[i][1]  # 바로 옆의 칸을 새로 변수로 설정.
            if 0 <= nr < N and 0 <= nc < N:  # 범위 안에 있는 칸이라면
                next = field[nr][nc]  # 옆 칸의 값을 저장.
                if next - current == 1:  # 옆 칸의 값과 현재 위치의 칸의 값의 차이가 1이라면
                    queue.append((nr, nc, cnt + 1))  # 그 칸을 queue 에 추가.
                    visited[nr][nc] = 1  # 이후 방문 표시.

    return cnt  # 순회가 끝났다면 칸 수를 반환.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N = int(input())  # 한 변의 길이를 입력.
    field = [list(map(int, input().split())) for _ in range(N)]  # 모든 방의 정보를 입력.
    result_num = N * N + 1  # 칸 수가 최대인 방의 번호를 얻기 위해 방 번호를 매우 크게 설정.
    result_cnt = 0  # 최대 칸 수를 얻기 위해 칸 수를 0으로 설정.

    for i in range(N):
        for j in range(N):  # 2차원 list 를 순회하면서
            num = field[i][j]  # 현재 위치의 값을 저장.
            count = bfs(i, j)  # 최대 칸 수를 세는 함수를 통해 최대 칸 수를 저장.
            if result_cnt < count:  # 최대 칸 수가 더 크다면
                result_num = num  # 그 칸의 번호를 저장하고,
                result_cnt = count  # 최대 칸 수도 저장.
            elif result_cnt == count:  # 최대 칸 수가 같다면
                if result_num > num:
                    result_num = num  # 칸의 번호가 작은 값을 저장.

    print(f'#{tc} {result_num} {result_cnt}')  # 양식에 맞게 출력.
