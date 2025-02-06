# View_조망권

T = 10  # test case의 갯수가 10개.

for i in range(1, T+1):
    
    N = int(input())  # 건물의 갯수를 받아옴
    arr = list(map(int, input().split()))  # 건물의 높이를 받아옴
    left_highest = 0  # 좌측, 우측을 나누어 생각하기 위해 좌측의 높은 건물을 인수로 지정.
    right_highest = 0  # 우측의 높은 건물을 인수로 지정.
    highest = 0  # left_highest, right_highest를 비교하여 나 이외에 가장 높은 건물을 찾음.
    right_of_a_view = 0  # 조망권 총합을 더하기 위해 인수를 설정.
    
    for j in range(2, N-2):  # 가장 왼쪽, 가장 오른쪽 두 칸은 반드시 0이기 때문에 그 사이 값만 비교하면 됨.
        
        ###########################################################################################################

        if arr[j-2] > arr[j-1]:  # 왼쪽의 가장 높은 건물을 찾는 부분.
            left_highest = arr[j-2]
        else:
            left_highest = arr[j-1]
        
        if arr[j+1] < arr[j+2]:  # 오른쪽의 가장 높은 건물을 찾는 부분.
            right_highest = arr[j+2]
        else:
            right_highest = arr[j+1]
        
        if left_highest > right_highest:  # left_highest와 right_highest를 비교하여 가장 높은 건물을 찾는 부분.
            highest = left_highest
        else:
            highest = right_highest

        ###########################################################################################################
        
        # 위 부분을 반복문으로 표현하면 더 짧아진다. 또한, 왼쪽과 오른쪽을 나눠서 계산할 필요도 없다.
        # 내가 왜 왼쪽과 오른쪽을 나눠서 하려고 했냐? continue의 존재를 잊고 있었기 때문.
        # continue를 알고 있었다면 반복문으로 짤 수 있었을텐데... 공부 더 하거나 continue, pass, break를 더 자주 쓰는 연습을 하자.
        
        if arr[j] > highest:  # 해당 건물과 비교하여 조망권을 더함.
            right_of_a_view += arr[j] - highest
            
    print(f'#{i} {right_of_a_view}')