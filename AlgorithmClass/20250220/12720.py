# 노드의 거리


def bfs(start, end):                        # 출발점에서 도착점까지 몇 개의 간선을 지나는지 찾는 함수
    queue = []                              # queue 만들기
    visited = [0] * (V + 1)                 # visited 만들기
    queue.append((start, 0))                # 현재 위치 enqueue
    visited[start] = 1                      # visited 에 방문 표시하기

    while queue:                            # queue 가 모두 없어질 때까지 반복
        current, far = queue.pop(0)         # queue 에서 현재 위치 pop
        if current == end:                  # 도착점에 도착했다면
            return far                      # 그 때까지 이동한 간선 갯수를 return.

        for i in range(1, V + 1):           # 모든 노드를 보면서
            if edges[current][i] == 1 and visited[i] == 0:  # 현재 위치와 연결되어 있고 방문한 적이 없다면
                queue.append((i, far + 1))  # 다음 움직일 위치에 넣어두고
                visited[i] = 1              # visited 에 방문 표시하기.

    return 0                                # 도착하지 못했을 때 0을 return


T = int(input())  # test case
for tc in range(1, T + 1):  # test case 만큼 반복

    V, E = map(int, input().split())  # 노드 갯수, 간선 갯수를 받음

    edges = [[0] * (V + 1) for _ in range(V + 1)]  # 연결된 정보를 표시하기 위해 빈 2차원 list 를 만듦.

    for _ in range(E):
        i, j = map(int, input().split())
        edges[i][j] = 1
        edges[j][i] = 1  # 간선 정보를 모두 표시함. 단방향 간선이 아니므로 양방향 위치를 모두 표시해 줌.

    S, G = map(int, input().split())  # 출발점, 도착점을 받음

    print(f'#{tc} {bfs(S, G)}')  # 양식에 맞게 출력