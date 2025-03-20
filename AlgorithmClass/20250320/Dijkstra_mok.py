'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''


def dijkstra(start, end):
    dist = [0xffffffff] * V  # 시작 정점에서 다른 정점까지의 비용.
    dist[start] = 0
    checked = set()
    # 모든 정점까지의 계산

    while len(checked) < V:
        min_v = -1
        min_dist = 0xffffffff

        for i in range(V):
            if i not in checked and dist[i] < min_dist:
                min_dist = dist[i]
                min_v = i

        checked.add(min_v)

        for i in range(V):
            if i not in checked and g[min_v][i] and g[min_v][i] + dist[min_v] < dist[i]:
                dist[i] = g[min_v][i] + dist[min_v]

    print(dist)


V, E = map(int, input().split())
g = [[0] * V for _ in range(V)]
for _ in range(E):
    start, end, weight = map(int, input().split())
    g[start][end] = weight

dijkstra(0, 5)
