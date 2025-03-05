# 이진 합

T = int(input())
for tc in range(1, T + 1):

    N = int(input())
    heap = [0] * (N + 1)
    heapcount = 0
    node = list(map(int, input().split()))
    summax = 0


    def heappush(v):
        global heapcount
        heapcount += 1
        heap[heapcount] = v
        current = heapcount
        parent = current // 2

        while True:

            if current == 1 or heap[current] > heap[parent]:
                break

            if heap[current] < heap[parent]:
                heap[current], heap[parent] = heap[parent], heap[current]

            current = parent
            parent = current // 2


    for i in range(N):
        heappush(node[i])

    while N > 1:
        summax += heap[N // 2]
        N = N // 2

    print(f'#{tc} {summax}')