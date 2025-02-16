# 그래프 경로


def solve(start, end):
    
    stack = [start]  # 먼저 start 가 들어있는 stack 을 하나 만들고
    visited = [0] * (V + 1)  # visited 라는 표시자를 만든다. 갯수는 V + 1 개로 만들어야 V 의 index 를 참고할 수 있음.
    # visited 의 index 를 각 node 의 번호라고 생각하자.
    visited[start] = 1  # stack 에 start 가 들어있으니, visited 에 표시를 해 준다.
    
    while stack:  # stack 이 비어있지 않을 때까지 반복. 다 돌고 나면 start 에서도 빠져 나와서 while 문이 멈춘다.
        top = stack[-1]  # stack 의 마지막 값을 참조. 후입선출이기 때문.
        
        if top == end:  # 목적지에 도착하면 stack 을 빼고 넣고 뭐 어쩌고 할 필요 없이 바로 멈춘다.
            return 1
        
        for i in range(1, V + 1):  # 이제 vertex 와 edge 를 정리한 list 를 활용할 차례.
            # 0번 index 는 볼 필요가 없다. 왜? 우리에겐 0번 node 가 없으니까.
            # 또한, 행은 top 으로 정해져 있다. 왜? 행이 즉 node 번호를 의미하니까.
            # 그러니까, 각 노드 번호에서(각 행에서) 어디로 이어져 있는지(edge) 각 열만 확인하면 이동이 가능.
            
            if list[top][i] and not visited[i]:  # list 에서 열만 확인하고, 그 곳에 들르지 않았다면(visited 를 1로 바꾸지 않았다면)
                stack.append(i)
                visited[i] = 1  # stack 에 현재 위치를 추가하고 visited 에 방문했다고 표시함
                break  # 이후 해당 반복문을 종료하여, 내 현재 위치의 행을 재탐색한다.
        
        else:  # 더 이상 이어진 곳이 없거나 내가 모든 이어진 곳을 방문한 경우
            stack.pop()  # 그 전 위치로 돌아가, 그 위치의 행에서 다른 이어진 곳을 재탐색.
    
    return 0  # stack 이 빈 경우, 즉 우리가 시작 index 에서 빠져 나온 경우 모든 곳을 탐색했다는 뜻.


T = int(input())

for tc in range(1, T + 1):

    V, E = map(int, input().split())

    list = [[0] * (V + 1) for _ in range(V + 1)]

    for edge in range(E):
        i, j = map(int, input().split())
        list[i][j] = 1

    S, G = map(int, input().split())
    
    print(f'#{tc} {solve(S, G)}')