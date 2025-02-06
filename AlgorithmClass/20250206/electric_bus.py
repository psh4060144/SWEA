# 전기 버스

T = int(input())

# 종점까지의 정류장 수 N, 한 번 충전으로 최대한 이동할 수 있는 정류장 수 K, 충전기가 설치된 정류장 갯수 M

for i in range(1, T + 1):

    K, N, M = list(map(int, input().split()))  # 인수 받는 부분. unpacking.
    arr = list(map(int,input().split()))  # 인수 받는 부분.
    count = [0] * (N + 1)  # N + 1개의 정류장 생성. 시작점 포함.
    result = 0  # 결과를 출력하기 위해 변수 설정.

    for j in range(len(arr)):  # N + 1개의 정류장 중 배터리가 있는 정류장만 counting.
        count[arr[j]] += 1  # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0] 처럼 나옴.

    charger = 0  # while 문의 반복을 멈추기 위해 인수를 설정.
    n = 1  # 위와 동일. 0번 자리에는 배터리가 있지만 세지 않으므로 1번 자리부터 시작.
    # 배터리를 충전한 곳의 다음 위치부터 K칸 움직일 수 있음.

    while n < N - K + 1:  # K칸 움직일 수 있으므로 마지막에 움직일 수 있는 칸의 수가 K를 넘어서면 멈춘다.

        how_many = 0  # 구간 K 이내의 배터리 갯수를 판단하기 위해 변수를 설정.
        
        for j in range(K):
            how_many += count[n + j]  # 구간 K 이내의 배터리 갯수를 count 변수를 이용해 모두 더한다.
        
        if how_many == 0:  # 배터리가 없다면 움직일 수 없다.
            result = 0  # 그 전까지 얻었던 모든 결과값을 지우고 break 한다.
            break
        else:
            for k in range(K):
               if count[n + k] == 1:  # 배터리가 있다면
                   charger = n + k    # 배터리 갯수가 1인 정류장의 index번호를 charger에 할당한다.
            n = charger + 1  # 해당 정류장 바로 다음 정류장부터 다시 시작하기 위해 + 1 한다.
            result += 1  # 결과값에 1을 더한다. 충전을 한 번만 하니까.
            
    print(f'#{i} {result}')