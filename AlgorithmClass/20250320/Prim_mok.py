'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''


# MST
# 1. 임의의 정점에서 시작
# 2. 갈 수 있는 경로 중 최소 비용 간선을 선택.
# 3. 선택한 정점을 MST 에 추가.
# 4. 선택한 정점들에서 선택할 수 있는 최소비용 선택.
# 5. 2~4 반복.
def prim():

    weights = [0xffffffff] * V
    weights[0] = 0
    MST = set()

    while len(MST) < V:
        min_weight = 0xffffffff
        min_v = -1

        for i in range(V):
            if i not in MST:  # 아직 선택되지 않은 정점이고
                if weights[i] < min_weight:
                    min_weight = weights[i]
                    min_v = i

        MST.add(min_v)  # 간선을 선택했으니 정점 저장.

        for i in range(V):
            if i not in MST and g[min_v][i] < weights[i]:
                weights[i] = g[min_v][i]

    return weights


V, E = map(int, input().split())
g = [[0xffffffff] * V for _ in range(V)]
for _ in range(E):
    start, end, weight = map(int, input().split())
    g[start][end] = weight
    g[end][start] = weight

print(prim())