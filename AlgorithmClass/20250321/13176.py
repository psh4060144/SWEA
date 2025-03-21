from heapq import heappush, heappop


def solve():
    # 시작 정점에서 다른 정점까지 가는 데 필요한 비용을 계산.
    # 특정 정점까지 비용이 확정난 정점을 재계산하는 일을 방지 및 비용 저장.
    visited = [[0] * N for _ in range(N)]
    weights = []
    heappush(weights, (0, (0, 0)))  # 비용, 위치(row, col). 왜 비용이 먼저냐? heapq 는 앞에 있는 값을 기준으로 뽑으니까.
    # 목적지까지의 비용이 확정될 때까지 반복하면서 비용 계산.
    while True:
        # 시작점에서 비용을 최소로 들여서 갈 수 있는 정점 구하기
        w, position = heappop(weights)
        # 비용이 확정나지 않은 경우
        if visited[position[0]][position[1]] == -1:
            visited[position[0]][position[1]] = w
        else:  # 확정했으니
            continue  # 다른 건 하지 않음.

        # 방금 확정된 정점을 거쳐 다른 정점으로 가는 비용을 계산
        # position 과 인접한 정점까지 가는 비용 계산. = 4방향 delta.
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = position[0] + dr, position[1] + dc
            if 0 <= nr < N and 0 <= nc < N:
                if data[nr][nc] > data[position[0]][position[1]]:
                    new_cost = 1 + data[nr][nc] - data[position[0]][position[1]]
                else:
                    new_cost = 1
                heappush(weights, (new_cost, (nr, nc)))


    pass


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 0, 0 에서 N - 1, N - 1까지 가는 최소 비용 계산.
    # dijkstra
