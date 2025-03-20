# Dijkstra
# 시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식.
# Prim 과 유사.
# 양수만 있는 그래프라면 최소 거리를 찾는 거긴 하지만, 최대 거리도 찾을 수 있다. 어떻게?
# 모든 숫자를 음수로 바꿔서 진행하면 된다!!!

# 벨만-포드, 플로이드 워셜: 다익스트라로 풀 수 없는 문제들(양수와 음수가 섞여 있는 그래프)을 풀기 위해 제작됨.
# 성능은 별로지만, 구현이 쉽다.


# heapq 사용, 가중치 초기화는 무한대 값으로.

import sys
import heapq

sys.stdin = open('dijkstra_input.txt', 'r')


def dijkstra(start_node):
    pq = [(0, start_node)]  # 누적 거리, 노드 번호
    dists = [INF] * V  # 각 정점까지의 최단 거리를 저장할 list
    dists[start_node] = 0  # 시작 노드의 최단 거리는 0

    while pq:
        dist, node = heapq.heappop(pq)

        # 이미 더 작은 경로로 온 적이 있다면 skip.
        if dists[node] < dist:
            continue

        for next_info in graph[node]:
            next_dist, next_node = next_info  # 다음 노드로 가기 위한 가중치, 다음 노드 번호.

            # 다음 노드로 가기 위한 누적 거리
            new_dist = dist + next_dist

            # 이미 같은 가중치거나, 더 작은 가중치로 온 적이 있다면 continue
            if dists[next_node] <= new_dist:
                continue

            # next_node 까지 도착하는 데 드는 비용은 new_dist.
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists


INF = int(21e8)
V, E = map(int, input().split())
start_node = 0
graph = [[] for _ in range(V)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))

# result_dists: 0에서 출발해서 다른 노드들까지의 최단 거리를 모두 구한다.
result_dists = dijkstra(0)
print(result_dists)
