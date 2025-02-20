# 미로 1


def find_start(arr):                                        # 시작점을 찾는 함수
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:                              # 2일 때(시작점일 때)의 좌표를 return.
                return i, j


def bfs(row, col):                                          # 출발지와 도착지가 연결되어 있는지 확인하는 함수.
    queue = [(row, col)]                                    # 2차원 배열이므로 출발지는 좌표로 주어짐.
    visited = [[0] * N for _ in range(N)]                   # 방문 표시도 2차원 배열로 해 주기 위해 2차원 배열을 만듦.
    visited[row][col] = 1                                   # 시작점을 방문했다고 표시

    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]                               # 북, 동, 남, 서 delta.

    while queue:                                            # queue 가 모두 없어질때까지 반복.
        current_row, current_col = queue.pop(0)             # 현재 위치의 좌표(행, 열)를 pop.
        if maze[current_row][current_col] == 3:             # 도착지에 도착할 수 있었다면 1을 return.
            return 1
        for direction in range(4):                          # 현재 위치에서 갈 수 있는 네 방향을 돌면서 확인
            next_row = current_row + delta_row[direction]
            next_col = current_col + delta_col[direction]   # 네 방향의 좌표를 찾아 그 값을 비교하는데,

            if 0 <= next_row < N and 0 <= next_col < N:     # 범위 안에 있고
                if maze[next_row][next_col] != 1 and not visited[next_row][next_col]:  # 벽이 아니며 방문하지 않은 곳이라면
                    queue.append((next_row, next_col))      # queue 에 그 방향의 좌표(행, 열)를 반환.
                    visited[next_row][next_col] = 1         # 그 방향을 방문했다고 표시.

    return 0                                                # 도착지에 도착하지 못했다면 0을 반환.


T = 10  # test case 는 10회로 고정.

for _ in range(1, T + 1):  # 10회 반복.

    N = 16  # 미로의 한 변의 길이는 16으로 고정.
    tc = int(input())  # 각 test case 의 번호를 받음.

    maze = [list(map(int, input())) for _ in range(N)]  # N 과 들어오는 정보를 이용해 미로를 만듦.

    start_row, start_col = find_start(maze)  # find_start 함수를 이용해 시작점의 위치(행, 열)을 찾음.

    print(f'#{tc} {bfs(start_row, start_col)}')  # bfs 함수를 사용한 값을 형식에 맞게 출력