T = 10  # test case는 10으로 고정.

for i in range(1, T+1):
    
    N = int(input())
    boxes = list(map(int, input().split()))
    
    for _ in range(N):  # N번 상자 옮기기
        max_idx = 0
        min_idx = 0

        # 상자 높이가 제일 높은 위치와 제일 낮은 위치 찾기
        for i in range(100):
            if boxes[i] >= boxes[max_idx]:
                max_idx = i
            elif boxes[i] <= boxes[min_idx]:
                min_idx = i
        
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
    
    # 상자 덤핑 끝

    max_idx = 0
    min_idx = 0

    # 상자 높이가 제일 높은 위치와 제일 낮은 위치 다시 찾기
    for i in range(100):
        if boxes[i] >= boxes[max_idx]:
            max_idx = i
        elif boxes[i] <= boxes[min_idx]:
            min_idx = i
    
    print(f'#{i} {boxes[max_idx] - boxes[min_idx]}')