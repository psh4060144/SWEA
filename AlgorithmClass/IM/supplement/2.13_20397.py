# 돌 뒤집기 게임 2

# idea 라기보다는 문제 해석
# 1. i 번째 돌은 i 번 index 의 돌을 말하는 것이 아니라, 맨 앞의 돌을 첫 번째 돌로 i - 1 번 돌을 의미하는 것.
# 2. 마주보는 j 개의 돌은 좌우로 넘어가면서 하나씩 세는 것.
# 3. 즉, 0 1 1 0 0 에서 i, j = [3, 1] 이 주어진다면, index 번호 상의 1번과 3번이 마주보고 있는 j개의 돌이다.
# 4. 같은 색, 다른 색의 기준은 저 돌 두 개를 보고 결정하는 거지, i 번 돌과는 상관이 없다.
# 5. 주어진 돌을 벗어나는 경우 뒤집기는 중지되는데, 안쪽부터 최대한 뒤집고 나서 중지된다.

T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))  # 주어진 정보를 받음

    for _ in range(M):
        i, j = list(map(int, input().split()))  # 한꺼번에 받지 않고 매 번 i, j 를 받아 와서 처리한다.
        # 기준 돌의 위치: i - 1
        
        for jj in range(1, j + 1):  # 1부터 범위를 잡아 i 본인을 계산에 포함시키지 않는다.
            
            if i - 1 - jj < 0 or i - 1 + jj > N - 1:  # 범위를 벗어나는 경우 중지.
                break
            
            if arr[i - 1 - jj] == arr[i - 1 + jj]:  # 벗어나지 않는 경우 돌을 뒤집는다.
                arr[i - 1 - jj] = (arr[i - 1 - jj] + 1) % 2
                
                # if arr[i - 1 - jj] == 0:
                #     arr[i - 1 - jj] = arr[i - 1 + jj] = 1  # 0 이면 1 로 뒤집고
                #     # arr[i - 1 - jj] = (arr[i - 1 - jj] + 1) % 2
                #     # arr[i - 1 + jj] = (arr[i - 1 + jj] + 1) % 2
                # else:
                #     arr[i - 1 - jj] = arr[i - 1 + jj] = 0  # 1 이면 0 으로 뒤집는다.
                #     # arr[i - 1 - jj] = (arr[i - 1 - jj] + 1) % 2
                #     # arr[i - 1 + jj] = (arr[i - 1 + jj] + 1) % 2

    print(f'#{tc}', end=' ')  # 형식에 맞게 출력
    for k in arr:
        print(k, end=' ')
    print()