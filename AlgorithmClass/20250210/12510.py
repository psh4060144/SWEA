# 특별한 정렬

T = int(input())  # test case

for i in range(1, T + 1):  # test case 번호를 위해 1, T + 1로 진행.

    N = int(input())  # 숫자 갯수

    ai = list(map(int, input().split()))  # 숫자를 list 형태로 받음
    L = len(ai)  # 받은 숫자 list의 길이

    for j in range(0, L, 2):  # 숫자가 두 개씩 동시에 정렬되기 때문에 2칸을 뛰어넘으며 정렬.
        max_idx = j  # max 값의 index 를 찾기 위해 변수 설정
        min_idx = j  # min 값의 index 를 찾기 위해 변수 설정
        
        for k in range(j + 1, L):  # max_idx를 찾는다.
            if ai[max_idx] < ai[k]:
                max_idx = k
        
        ai[j], ai[max_idx] = ai[max_idx], ai[j]  # max_idx와 홀수 번째 요소를 교환.
        
        for l in range(j + 1, L):  # min_idx를 찾는다.
            if ai[min_idx] > ai[l]:
                min_idx = l
        
        if j + 1 >= L:  # list의 길이를 넘어가는 경우 위치를 바꾸지 않고 종료.
            break
        else:
            ai[j + 1], ai[min_idx] = ai[min_idx], ai[j + 1]  # min_idx와 짝수 번째 요소를 교환.
        
    print(f'#{i}', end = ' ')
    if L > 10:
        for m in range(10):
            print(ai[m], end = ' ')
    else:
        for m in range(L):
            print(ai[m], end = ' ')
    print('')