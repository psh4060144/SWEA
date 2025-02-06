T = 10

for i in range(1, T+1):

    N = int(input())
    arr = list(map(int, input().split()))
    count = [0] * 101  # 가로 길이가 항상 100이므로 요소를 101개(0~100) 가지는 인수 생성.
    
    for j in range(100):
        count[arr[j]] += 1

    for _ in range(N):
        
        left = 0
        right = 100
        
        while count[left] == 0:
            left += 1
        
        while count[right] == 0:
            right -= 1
        
        count[left] -= 1
        count[left + 1] += 1
        count[right] -= 1
        count[right - 1] += 1
        
    left = 0
    right = 100
    
    while count[left] == 0:
        left += 1
        
    while count[right] == 0:
        right -= 1

    print(f'#{i} {right-left}')