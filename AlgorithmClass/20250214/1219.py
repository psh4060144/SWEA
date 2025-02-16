# 길찾기


def route(start, end):  # start 부터 end 까지 가는 길이 있는지 찾는 함수
    stack = [start]  # 현재 있는 위치를 표시하기 위해 stack 을 만듦.
    visit = [0] * (end + 1)  # 방문할 수 있는 위치 만큼의 표시자를 만듦.
    visit[start] = 1  # 현재 node 에 도착했다는 의미로 해당 index 에 표시.
    
    while stack:  # stack 이 비워지기 전까지 반복
        top = stack[-1]  # 현재 위치를 갱신
        
        if top == end:  # 현재 위치가 마지막 위치라면 1을 return.
            return 1
        
        for i in range(100):  # 현재 위치가 마지막 위치가 아니기 때문에 반복구문을 돌림
            if adj[top][i] == 1 and visit[i] == 0:  # 현재 위치에서 갈 수 있는 가장 작은 index 의 node 중 가지 않은 곳이 있다면
                stack.append(i)  # 그 곳으로 가서
                visit[i] = 1  # visit index 에 표시.
                break  # 그리고 while 문으로 돌아감.
        
        else:
            stack.pop()  # 더 이상 현재 위치에서 갈 수 있는 node 가 없다면 그 전 위치로 돌아감.
    
    return 0  # stack 이 다 비워졌다 == 마지막 위치까지 가는 길이 없어 처음 위치에 돌아왔다. 따라서 0 return.


T = 10  # test case 는 10으로 고정.

for _ in range(T):  # test case 만큼 반복

    tc, E = map(int, input().split())  # test case 번호, edge 갯수를 입력.

    adj = [[0] * 100 for _ in range(100)]  # 최대 100개의 node 가 들어올 수 있으므로, node 를 표시해주기 위해 100 * 100 의 행렬이 필요함.
    edge_full = list(map(int, input().split()))  # 총 edge 를 list 형태로 받음.

    for k in range(0, len(edge_full) - 1, 2):  # 받은 edge list 를 두 칸씩 뛰어넘으며 읽어 adj 에 표시해 주어야 한다.
        i, j = edge_full[k], edge_full[k + 1]  # 두 칸 마다의 값을 받아
        adj[i][j] = 1  # i 에서 j 로 가는 edge 를 adj 에 표시해 줌. 

    print(f'#{tc} {route(0, 99)}')  # 함수 실행. start 지점은 0, end 지점은 99.