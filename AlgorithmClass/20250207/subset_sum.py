T = int(input())  # test case의 총 갯수
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # 집합 A를 표현.
L = len(arr)  # 이렇게 안 해도 되지만, arr의 길이가 변할 때 이렇게 쓰면 된다.
new_list = []  # 갯수가 N인 list를 거르기 위해 빈 list를 생성.

for i in range(1, T+1):  # 반복

    N, K = list(map(int, input().split()))  # 원소의 갯수 N, 원소의 합 K
    sum = 0  # 원소의 합을 구하기 위해 변수를 생성.
    sum_count = 0  # 원소 합이 K와 일치하는지 알아보는 변수를 생성.

    for j in range(1 << L):   # 부분 집합의 갯수만큼 반복. 2 ** L == 1 << L
        for k in range(L):  # 원소의 수만큼 bit을 비교.
            if j & (1 << k):  # j의 k번 bit이 1인 경우. 즉, 해당 bit의 1이 있는 자릿수를 출력.
                new_list.append(arr[k])  # new_list에 추가.
        
        if len(new_list) == N:  # new_list의 길이가 N인 경우에만
            for l in range(N):
                sum += new_list[l]  # list의 모든 요소를 더해
            if sum == K:
                sum_count += 1  # K와 비교.
                
        sum = 0
        new_list = []  # 다음 루프를 위해 sum과 new_list는 청소.

    print(f'#{i} {sum_count}')