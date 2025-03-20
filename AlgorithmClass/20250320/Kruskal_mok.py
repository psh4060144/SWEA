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


def kruskal():
    # 간선을 선택할 때 cycle 이 생기지 않도록 선택해야 함.
    MST = []

    # 간선을 가중치 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    for i in range(E):
        if find_set(edges[i][0]) != find_set(edges[i][1]):
            # 둘이 같으면 같은 집합이므로 cycle 이 생긴다.
            MST.append(edges[i])
            union(edges[i][0], edges[i][1])

    print(MST)


def union(x, y):
    rx = find_set(x)
    ry = find_set(y)
    p[rx] = ry


def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])


V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E)]
# cycle 확인을 위해 disjoint set 만들기. 즉, union 해야 한다.
p = [x for x in range(V)]

kruskal()
