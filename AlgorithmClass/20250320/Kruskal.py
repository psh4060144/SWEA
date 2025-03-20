# Kruskal algorithm
# 1. 모든 간선을 가중치에 따라 오름차순으로 정렬.
# 2. 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴. 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택.
# 3. 간선의 갯수가 n-1개가 될 때까지 2를 반복.

import sys

sys.stdin = open('lecture_input.txt', 'r')


def find_set(x):  # 대표자 검색
    if x == parents[x]:  # 내가 대표라면
        return x  # 나를 뽑는다.
    # return find_set(x)  # 아니라면 대표를 찾으러 간다. 근데... 너무 오래 걸린다.
    parents[x] = find_set(parents[x])  # 경로 압축!
    return parents[x]


def union(x, y):  # x, y를 같은 집합으로 만들어 줌.
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:  # 사이클링 방지.
        return

    if ref_x < ref_y:  # 연결된 집합의 모든 요소 중 대표자는 아무나 해도 된다. 그러니까, 제일 작은 애 시키자.
        parents[ref_x] = ref_y
    else:
        parents[ref_y] = ref_x


V, E = map(int, input().split())
edges = []

for _ in range(E):
    start, end, weight = map(int, input().split())
    # 간선에 대한 정보들을 저장.
    edges.append((start, end, weight))

edges.sort(key=lambda x: x[2])  # 가중치 기준으로 오름차순 정렬.
parents = [i for i in range(V)]  # Union 의 make_set (정점을 기준으로 만들어 줌).

# 작은 것부터 고르면서 나아간다. 언제까지? N - 1 개를 고를 때까지!
cnt = 0  # 선택한 간선의 수
result = 0  # 가중치의 합

for start, end, weight in edges:
    # u 와 v 가 연결되어 있지 않다면 선택. 즉, 서로 다른 집합에 있다면 선택.
    if find_set(start) != find_set(end):
        union(start, end)
        cnt += 1
        result += weight

        if cnt == V - 1:  # 간선을 모두 골랐다면
            break

print(result)


########################
# Prim vs Kruskal
# Prim: O((V + E) * logV) / Kruskal: O(E * logE)

# Prim: 보통 정점보다 간선이 더 많다. 따라서 일반화하면 O(E * logV). 간선의 수가 적을 때 유리하다.
# Kruskal: 간선 위주로 정렬해서 최소를 뽑는다. 간선의 수가 많을 때 유리하다.

# 즉, 간선의 갯수가 적다면 Prim, 간선의 갯수가 많다면 Kruskal 을 사용하는 게 유리하다.
