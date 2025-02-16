# 그래프 경로


def route(S, G):
    stack = [S]  # stack 의 마지막 요소를 우리의 현재 위치로 적용.
    visit = [0] * (V + 1)  # V + 1 개의 요소로 이루어진 list 를 만들어서 방문했는지 체크.
    visit[S] = 1  # 시작점은 방문하고 들어가니까 방문에 체크.
    
    while stack:  # 현재 위치가 없어지면 다 돌고 처음 시작점 바깥으로 나간 것.
        top = stack[-1]  # stack 의 마지막 요소 = 현재 위치
        
        if top == G:  # 현재 위치가 도착점이면 갈 수 있으므로 1 return.
            return 1
        
        for i in range(1, V + 1):  # 도착점이 아니라면 해당 위치의 edge 를 돌아가며 검색해서
            if adj[top][i] == 1 and visit[i] != 1:  # 가지 않았던 곳에 이어지는 edge 라면
                stack.append(i)  # stack 에 추가함으로써 새 위치를 정함.
                visit[i] = 1  # 또한 새 위치을 방문에 체크.
                break
        
        else:
            stack.pop()  # 이어지는 edge 가 없거나 모두 가 봤던 곳이라면 그 전 위치로 돌아가기 위해 현재 위치를 제거.
        
    return 0  # 모든 위치가 제거되면 while 문이 종료되므로, 그 땐 갈 수 없는 것이므로 0 return.


T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    V, E = map(int, input().split())  # vertex, edge 를 받음
    adj = [[0] * (V + 1) for _ in range(V + 1)]  # edge 표현하기 위해 빈 list 를 만들어 줌. vertex 만큼의 크기로.

    for _ in range(E):
        i, j = map(int, input().split())  # 모든 edge 를 list 내에 반영해 줌.
        list[i][j] = 1

    S, G = map(int, input().split())  # start, goal 을 받음.

    print(f'#{tc} {route(S, G)}')  # 함수 실행.