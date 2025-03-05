# 미로의 거리


def find_start(arr):                                        # 시작점을 찾는 함수
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:                              # 2일 때(시작점일 때)의 좌표를 return.
                return i, j


def bfs(row, col):                                          # 출발지부터 도착지까지의 칸 수를 세는 함수.
    queue = [(row, col, 0)]                                 # 2차원 배열이므로 출발지는 좌표로 주어짐. 움직인 거리도 0으로 주어짐.
    visited = [[0] * N for _ in range(N)]                   # 방문 표시도 2차원 배열로 해 주기 위해 2차원 배열을 만듦.
    visited[row][col] = 1                                   # 시작점을 방문했다고 표시

    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]                               # 북, 동, 남, 서 delta.

    while queue:                                            # queue 가 모두 없어질때까지 반복.
        current_row, current_col, far = queue.pop(0)        # 현재 위치의 좌표(행, 열), 움직인 거리를 pop.
        if maze[current_row][current_col] == 3:             # 도착지에 도착했다면
            return far - 1                                  # 시작점과 끝점을 제외하고 움직인 칸 수를 return.
        for direction in range(4):                          # 현재 위치에서 갈 수 있는 네 방향을 돌면서 확인.
            next_row = current_row + delta_row[direction]
            next_col = current_col + delta_col[direction]   # 네 방향의 좌표를 찾아 그 값을 비교하는데,

            if 0 <= next_row < N and 0 <= next_col < N:     # 범위 안에 있고
                if maze[next_row][next_col] != 1 and not visited[next_row][next_col]:  # 벽이 아니며 방문하지 않은 곳이라면
                    queue.append((next_row, next_col, far + 1))  # queue 에 그 방향의 좌표(행, 열), 움직인 칸 수 + 1 을 반환.
                    visited[next_row][next_col] = 1         # 그 방향을 방문했다고 표시.

    return 0                                                # 도착지에 도착하지 못했다면 0을 반환.


T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    N = int(input())  # 미로의 한 행의 칸 수를 입력.

    maze = [list(map(int, input())) for _ in range(N)]  # N 과 들어오는 정보를 이용해 미로를 만듦.

    start_row, start_col = find_start(maze)  # find_start 함수를 이용해 시작점의 위치(행, 열)을 찾음.

    print(f'#{tc} {bfs(start_row, start_col)}')  # bfs 함수를 사용한 값을 형식에 맞게 출력