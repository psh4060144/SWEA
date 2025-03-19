import sys
sys.stdin = open('input.txt', 'r')


def dfs(node):
    # 보통 graph 문제들에서, 여기 바로 아래에는 가지치기가 들어간다.

    print(node, end=' ')
    # 내가 갈 수 있는 모든 후보를 진행하면서 한 군데로 진행.
    # = 현재 노드에서 인접한 노드들을 모두 확인하면서, 한 군데로 진행.
    for next_node in graph[node]:
        if visited[next_node]:
            continue

        visited[next_node] = 1
        dfs(next_node)


def bfs(start_node):
    q = [start_node]  # 시작값을 넣은 상태로 출발
    # 1. 가장 앞의 노드를 뽑음
    # 2. 해당 노드에 자식이 없을때까지 진행.
    while q:
        now = q.pop()

        for next_node in graph[now]:
            if visited[next_node]:
                continue

            visited[next_node] = 1
            q.append(next_node)


N, M = map(int, input().split())

# 1. 그래프 저장. 2. 빈 그래프 생성 후, 그래프 정보를 입력.

# 인접 list 형식으로 문제 풀이.
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)  # 양방향 노드라면, 반대쪽도 저장해주어야 함.

visited = [0] * (N + 1)
visited[1] = [1]

dfs(1)
bfs(1)