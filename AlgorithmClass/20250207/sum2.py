# sum

T = 10  # test case는 10개

for i in range(T):  # 어차피 각 test case의 번호가 들어오므로(N) 굳이 1, T + 1로 안해도 된다.
    
    N = int(input())  # test case의 번호. 이거 그대로 마지막에 출력.
    sum = 0  # 합계의 최댓값을 구하기 위해 인수를 설정.
    col_sum = [0] * 100  # 열의 최댓값을 구하기 위해 0이 100개인 list 설정.
    left_to_right = 0  # 오른쪽 아래로 내려가는 대각선은 매 입력마다 0에서 우측으로 한 칸씩 이동하며 더하면 된다.
    right_to_left = 0  # 왼쪽 아래로 내려가는 대각선은 매 입력마다 99에서 좌측으로 한 칸씩 이동하며 더하면 된다.
    
    for j in range(100):  # 100개의 list를 받음
        
        arr = list(map(int, input().split()))
        row_sum = 0  # 행의 최댓값을 구하기 위해 인수를 설정. 
                
        for k in range(100):  # 받으면서 행 덧셈은 바로 수행. 
            row_sum += arr[k]
            if sum < row_sum:  # 행 합계의 최댓값은 바로 판별 후 대입.
                sum = row_sum
        
        for l in range(100):
            col_sum[l] += arr[l]  # 열 합계는 0이 100개인 list에 각각 더한다.
        
        left_to_right += arr[j]
        right_to_left += arr[99 - j]  # 대각선은 각각 숫자만 더한다.
    
    for j in range(100):  # 모든 열 합계를 비교하기 위해 다시 for문을 사용.
        if sum < col_sum[j]:
            sum = col_sum[j]
    
    if sum < left_to_right:  # 대각선은 각각 숫자만 비교한다.
        sum = left_to_right
    
    if sum < right_to_left:
        sum = right_to_left
    
    print(f'#{N} {sum}')