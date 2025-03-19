# 경로의 수


def dfs(node):  # 도착점까지의 경로 갯수를 세는 함수.
    global cnt  # 경로를 세기 위해 전역 변수를 설정.

    if node == G:  # 도착했다면
        cnt += 1  # 경로 갯수를 추가.
        return  # 이후 종료.

    for next_node in graph[node]:  # 현재 노드에서 갈 수 있는 노드를 보는데
        if visited[next_node] == 1:  # 이미 갔던 노드라면
            continue  # 다음 노드를 확인.

        visited[next_node] = 1  # 가지 않은 노드라면 노드에 방문 표시를 해 주고
        dfs(next_node)  # 그 노드에서 다시 경로를 확인.
        visited[next_node] = 0  # 경로 확인이 끝났다면 방문 표시 제거.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N, E = map(int, input().split())  # 정점 번호 N, 간선 수 E 입력.
    edge = list(map(int, input().split()))  # 모든 간선 정보 입력.
    S, G = map(int, input().split())  # 시작점 S, 끝점 G 입력.
    graph = [[] for _ in range(N + 1)]  # 간선 연결 정보를 2차원 list 로 표현하기 위해 list 를 설정.
    cnt = 0  # 경로 갯수를 세기 위해 변수를 설정.

    for i in range(0, E * 2, 2):  # 두 칸씩 뛰면서
        start, goal = edge[i], edge[i + 1]  # 간선의 시작점과 끝점을 확인해서
        graph[start].append(goal)  # 그대로 list 에 추가.

    visited = [0] * (N + 1)  # 방문 표시를 위해 list 를 설정.
    visited[S] = 1  # 출발점에 방문 표시.
    dfs(S)  # 도착점까지의 경로 갯수를 세는 함수 실행.

    print(f'#{tc} {cnt}')  # 양식에 맞게 출력.
