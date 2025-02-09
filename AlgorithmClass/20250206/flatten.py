T = 10  # test case는 10으로 고정.

for i in range(1, T+1):
    
    N = int(input())
    arr = list(map(int, input().split()))
    count = [0] * 100  # 상자의 높이가 1 ~ 100이므로 100개의 요소를 가진 count를 생성. 여기서, 각 상자의 높이에 해당하는 index는 count[x - 1]임에 유의.
                       # 즉, 1 ~ 100의 숫자가 0 ~ 99에 들어감.
    
    for j in range(0, 100):  # 100번 반복하여
        count[arr[j]-1] += 1  # 1씩 차이나는 올바른 자리에 count를 추가.
    
    min = 0  # 최솟값의 갯수
    max = 99  # 최댓값의 갯수
    
    for _ in range(N):  # 덤프 횟수만큼 반복
        
        while count[min] == 0:  # 최솟값의 갯수가 0이 아닌 값을 찾아감.
            min += 1
        
        while count[max] == 0:  # 최댓값의 갯수가 0이 아닌 값을 찾아감.
            max -= 1            
        
        count[min + 1] += 1
        count[min] -= 1
        count[max - 1] += 1  # 덤프를 수행하면 최댓값과 최솟값의 갯수는 하나씩 줄고, (최댓값-1)과 (최솟값+1)은 하나씩 늚.
        count[max] -= 1      # 따라서, 24 ~ 27 line을 통해 덤프 1회 시 변하는 갯수를 반영.
    
    # while count[min] == 0:  # 마지막 덤프에서 최솟값의 갯수가 0이 될 때 (최솟값+1)이 새로운 최솟값이 되는데 그걸 반영하지 않는 오류가 발생했음.
    #     min += 1            # 따라서, 한 번 더 최솟값을 찾아주는 반복문을 수행. 마지막에 한 번만 찾으면 되기 때문에 for 문 안에서 쓸 이유가 없음.

    # while count[max] == 0:  # 최댓값의 경우에도 마찬가지이므로, 한 번 더 최댓값을 찾아주는 반복문을 수행.
        # max -= 1    
    
    print(f'#{i} {max-min}')
    