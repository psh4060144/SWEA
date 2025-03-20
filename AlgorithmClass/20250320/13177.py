# 최소 이동 거리


def dijkstra(start, goal):  # 최소 이동 거리를 구하는 함수.
    dist = [0xffffffff] * N  # 일단 각 노드까지 갈 수 있는 최소 이동 거리가 더 작을 때 갱신하므로 매우 큰 값을 잡아줌.
    dist[start] = 0  # 시작점에서의 최소 이동 거리는 0이므로 0 입력.
    check = set()  # 각 정점 중 최소 거리를 구한 정점만 set 에 기입.

    while len(check) < N:  # 모든 노드를 들를 때까지 반복.
        min_v = -1  # 매 노드에 연결된 다른 노드 중 최소 거리인 노드를 저장.
        min_dist = 0xffffffff  # 그 노드까지의 거리를 저장.

        for i in range(N):  # 모든 노드를 보면서
            if i not in check and min_dist > dist[i]:  # 간 적 없고 그 노드까지의 거리가 다른 모든 연결된 노드보다 짧다면
                min_dist = dist[i]  # 그 노드까지의 거리가 최소 이동 거리이므로 죄소 이동 거리에 기입.
                min_v = i  # 최소 거리인 노드를 저장.

        check.add(min_v)  # 최소 거리 노드를 set 에 기입.

        for i in range(N):  # 다시 모든 노드를 보면서
            # 들른 적 없고, 연결되어 있으며, 그 노드까지의 최소 이동 거리가 다른 노드를 경유하는 것보다 크다면
            if i not in check and graph[min_v][i] and dist[i] > graph[min_v][i] + dist[min_v]:
                dist[i] = graph[min_v][i] + dist[min_v]  # 최소 이동 거리를 교체.

    return dist[goal]  # 최소 이동 거리가 구해지므로 그대로 반환.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N, E = map(int, input().split())  # 마지막 정점 번호 N, 도로 갯수 E 입력.
    N += 1  # 마지막 정점 번호 + 1 개만큼 노드가 존재하므로 계산하기 편하게 1을 더해 줌.
    graph = [[0] * N for _ in range(N)]  # 도로 연결 정보, 도로 길이를 표시하기 위해 2차원 list 설정.
    for _ in range(E):  # 도로 갯수만큼 반복하면서
        start, end, weight = map(int, input().split())  # 도로의 정보(시작점, 끝점, 거리)를 입력.
        graph[start][end] = weight  # 입력된 도로의 정보를 그대로 graph 에 기입.

    result = dijkstra(0, N - 1)  # 최소 이동 거리를 구하는 함수 실행.
    print(f'#{tc} {result}')  # 양식에 맞게 출력.
