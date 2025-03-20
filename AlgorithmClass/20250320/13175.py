# 최소 신장 트리


def kruskal():  # 최소 신장 트리의 간선 가중치를 kruskal 알고리즘으로 구하는 함수.
    weight = 0  # 가중치를 0으로 설정.

    graph.sort(key=lambda x: x[2])  # 모든 간선을 가중치를 기준으로 정렬.

    for i in range(E):  # 앞에서부터 순회하면서
        if find_set(graph[i][0]) != find_set(graph[i][1]):  # 간선의 시작점과 끝점이 같은 그룹이 아니라면
            weight += graph[i][2]  # 가중치를 더해주고,
            union(graph[i][0], graph[i][1])  # 둘을 같은 그룹으로 설정.

    return weight  # 가중치 반환.


def find_set(x):  # 대표자를 선택하는 함수.
    if x == p[x]:  # 노드의 대표자가 자기 자신이라면
        return x  # 자신이 대표자이므로 반환.
    else:  # 아니라면
        return find_set(p[x])  # 연결된 노드의 대표자를 찾음.


def union(x, y):  # 같은 그룹으로 설정하는 함수.
    rx = find_set(x)  # x 의 대표자를 확인.
    ry = find_set(y)  # y 의 대표자를 확인.
    p[rx] = ry  # x 의 대표자를 y 의 대표자와 같게 한다.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    V, E = map(int, input().split())  # 마지막 노드 번호 V, 간선 갯수 E 입력.
    V += 1  # 마지막 정점 번호 + 1 개만큼 노드가 존재하므로 계산하기 편하게 1을 더해 줌.
    graph = [tuple(map(int, input().split())) for _ in range(E)]  # 모든 간선 정보를 tuple 형태로 입력.
    p = [x for x in range(V)]  # 대표자를 표시하기 위해 list 를 제작.

    result = kruskal()  # 최소 신장 트리의 간선 가중치를 구하는 함수 실행.
    print(f'#{tc} {result}')  # 양식에 맞게 출력.