# 그룹 나누기


def dfs(node):  # 조 갯수를 세는 함수.
    global visited  # 모든 학생을 확인하기 위해 전역 변수를 설정.

    for next_node in graph[node]:  # 해당 학생과 같은 조를 하고 싶어하는 학생을 모두 보는데
        if not visited[next_node]:  # 그 학생이 다른 조에 속해있지 않다면
            visited[next_node] = 1  # 그 학생을 조에 포함하고
            dfs(next_node)  # 해당 학생과 같은 조를 하고 싶어하는 다른 학생을 확인.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N, M = map(int, input().split())  # N 번까지의 출석번호(노드 갯수), M 장의 신청서(간선 갯수)
    edge = list(map(int, input().split()))  # 신청서 정보를 받음.
    graph = [[] for _ in range(N + 1)]  # 간선 연결 정보를 2차원 list 로 표현하기 위해 list 를 설정.

    for i in range(0, M * 2, 2):  # 두 칸씩 뛰면서
        start, end = edge[i], edge[i + 1]  # 신청서 정보를 받아서
        graph[start].append(end)  # list 에 입력.
        graph[end].append(start)  # 방향이 없는 간선이므로 반대쪽으로도 입력.

    visited = [0] * (N + 1)  # 학생 확인 표시를 위해 list 를 설정.
    cnt = 0  # 조 갯수를 세기 위해 변수를 설정.

    for i in range(1, N + 1):  # 모든 학생을 돌면서
        if not visited[i]:  # 조가 없는 학생은
            visited[i] = 1  # 조를 편성하고
            dfs(i)  # 그 학생과 같은 조를 하고 싶어하는 다른 학생도 같이 편성.
            cnt += 1  # 그 후 조 갯수를 추가.

    print(f'#{tc} {cnt}')  # 양식에 맞게 출력.
