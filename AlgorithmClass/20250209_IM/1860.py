# 진기의 최고급 붕어빵

T = int(input())

for i in range(1, T + 1):

    N, M, K = list(map(int, input().split()))  # 손님 수, 만드는 시간, 만드는 갯수.
    arr = list(map(int, input().split()))  # 각 손님 방문 시간.
    arr_idx = [0] * 11112  # 최대 11111초 안에 도착하므로 11111개의 빈 index를 만듦.
    validate = 1  # 유효한지 판단하기 위해 변수를 설정.
    fish = 0  # 붕어빵 갯수를 설정.
    
    for j in range(len(arr)):
        arr_idx[arr[j]] += 1  # 각 손님들의 방문 시간을 index로 저장.

    for k in range(len(arr_idx)):
        
        if k == 0:  # 손님이 0초에 오는 경우 붕어빵이 없다.
            pass
        elif k % M == 0:  # 만드는 시간이 끝날때마다 붕어빵 갯수를 추가.
            fish += K
        
        fish = fish - arr_idx[k]  # 붕어빵을 주는데,
        
        if fish < 0:              # 붕어빵 갯수가 사람 수를 충족하지 못한다면
            validate = 0          # 유효 판단 변수를 0으로 하고
            break                 # 그대로 종료.
    
    if validate == 1:  # 붕어빵 갯수가 사람 수를 모두 충족했다면 possible 출력.
        print(f'#{i} Possible')
    else:
        print(f'#{i} Impossible')