# 이진 힙

T = int(input())  # test case
for tc in range(1, T + 1):  # test case 만큼 반복

    N = int(input())  # node 갯수 입력
    heap = [0] * (N + 1)  # node 갯수만큼의 heap 제작. 0부터 시작하게 만들기 위해 N + 1 개로.
    heapcount = 0  # heap 에 저장할 수 있게 node 와는 다른 indexing 변수를 추가.
    node = list(map(int, input().split()))  # 모든 node 정보를 받음.
    summax = 0  # 모든 조상 node 를 더하기 위해 변수 설정.


    def heappush(v):  # heap 에 저장하는 함수.
        global heapcount  # indexing 변수를 전역 변수로 설정
        heapcount += 1  # node 를 추가할 때마다 heapcount 를 늘려줌.
        heap[heapcount] = v  # heap 의 마지막에 node 를 추가.
        current = heapcount  # 현재 위치를 추가한 node 의 위치로 설정.
        parent = current // 2  # 부모 node 를 설정.

        while True:
            if current == 1 or heap[current] > heap[parent]:  # root node 가 되거나 부모 node 보다 큰 경우
                break  # 멈춤.

            if heap[current] < heap[parent]:  # 부모 node 보다 작은 경우
                heap[current], heap[parent] = heap[parent], heap[current]  # 부모 node 와 현재 node 의 위치를 바꿈.

            current = parent  # 현재 node 가 부모 node 가 되었으므로 현재 node 를 바꿔 줌.
            parent = current // 2  # 다시 현재 node 의 부모 node 를 설정.


    for i in range(N):  # 모든 node 에 대해
        heappush(node[i])  # heap 에 저장.

    while N > 1:  # N 이 마지막 node 이므로 N 이 root node 가 될 때까지 반복.
        summax += heap[N // 2]  # N 의 부모 node 의 값을 더해 줌.
        N = N // 2  # 이후 부모 node 로 이동.

    print(f'#{tc} {summax}')  # 양식에 맞게 출력.