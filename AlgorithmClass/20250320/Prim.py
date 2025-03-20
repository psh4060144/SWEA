# 최소 신장 트리 Minimum Spanning Tree.

# 신장 트리
# 연결된 그래프 내에서 만들어질 수 있는,
# 1. 모든 정점을 연결하고, 사이클이 없는 tree (N >= 3).
# 즉, 하나의 그래프에서 여러 가지의 신장 트리가 나올 수 있다.

# prim: 정점을 기준으로 생각. / kruskal: 간선을 기준으로 생각.

# prim algorithm
# 하나의 정점에서 연결된 간선들 중 하나씩 선택하면서 MST 를 만들어가는 방식.
# 1. 임의의 정점을 하나 선택
# 2. 선택한 정점과 인접하는 정점들 중의 최소 비용의 간선(가중치가 가장 작은 간선)이 존재하는 정점을 선택.
# 3. 모든 정점이 선택될 때까지 1, 2를 반복.
# 즉, BFS 를 돌리면서 같은 층 내의 가중치가 제일 작은 것만 선택하는 것.

import sys, heapq
sys.stdin = open('lecture_input.txt', 'r')


def prim(start):
    pq = [(0, start)]  # 시작점은 가중치가 0이다.
    MST = [0] * V  # visited 와 동일.
    min_weight = 0  # 최소 비용 저장.

    while pq:
        weight, node = heapq.heappop(pq)

        # 이미 방문한 노드는 다시 볼 필요가 없다.
        if MST[node]:
            continue

        MST[node] = 1
        min_weight += weight

        for next_node in range(V):
            # 갈 수 없다면 pass
            if graph[node][next_node] == 0:
                continue
            # 이미 방문했다면 pass
            if MST[next_node]:
                continue

            heapq.heappush(pq, (graph[node][next_node], next_node))

    return min_weight


V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight

result = prim(0)
print(result)
