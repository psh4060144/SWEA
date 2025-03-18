import heapq

arr = [20, 15, 19, 4, 13, 11]

# 1. heap 제작.
heapq.heapify(arr)  # 최소 heap 제작.
print(arr)

# heap tree 가 구현이 되어 있다!
# heap 의 단점: 디버깅이 어렵다...
# 왜? 이진 트리의 형식으로 제작이 되기 때문에. 즉, 딱 봤을 때는 정렬이 안 된 것처럼 보인다....

# 2. heap 에 데이터를 추가.
min_heap = []
for num in arr:
    heapq.heappush(min_heap, num)
print(min_heap)

# 3. heap 에서 데이터 꺼내기.
while min_heap:
    pop_num = heapq.heappop(min_heap)
    print(pop_num, end=' ')
print()

# 최대 힙을 만드는 방법은?
max_heap = []
for num in arr:
    heapq.heappush(max_heap, -num)
print(max_heap)

while max_heap:
    pop_num = heapq.heappop(max_heap)
    print(-pop_num, end=' ')
print()
