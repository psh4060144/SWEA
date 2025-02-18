def solve():
    # 0번에서 99번으로 가는 길이 있느냐?
    # 0번에서 시작하는 완전탐색 >>> DFS
    stack = [0]
    visited = [0] * 100
    visited[0] = 1

    while stack:
        current = stack[-1]
        if current == 99:
            return 1
        # 현재 정점에서 연결된 정점 정보는 graph 가 가지고 있다. 따라서 graph[current]를 보면 된다.
        
        if graph[current][0] != -1 and not visited[graph[current][0]]:
            stack.append(graph[current][0])
            visited[graph[current][0]] = 1
        elif graph[current][0] != -1 and not visited[graph[current][1]]:
            stack.append(graph[current][1])
            visited[graph[current][1]] = 1
        else:  # 연결 정보 2열을 모두 봤는데도 갈 수 있는 경로가 없다면,
            stack.pop()

    return 0

T = 10
for _ in range(T):
    tc, E = map(int, input().split())
    graph = [[-1] * 2 for _ in range(100)]
    # 행의 index: 정점 번호.
    # 각 열의 요소: 정점과 연결된 다른 정점의 번호.

    data = list(map(int, input().split()))
    
    for i in range(0, E * 2, 2):
        data[i], data[i + 1]
        if graph[data[i]][0] != -1:
            graph[data[i]][1] = data[i + 1]
        else:
            graph[data[i]][0] = data[i + 1]
    
result = solve()
print(F'#{tc} {result}')