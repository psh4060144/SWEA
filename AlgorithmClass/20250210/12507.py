# 이진 탐색

T = int(input())  # test case

for i in range(1, T + 1):  # test case 번호를 위해 1, T + 1로 진행.

    P, Pa, Pb = list(map(int, input().split()))  # 책 장수, a의 목표 페이지, b의 목표 페이지를 받음

    start = 1
    end = P
    a_count = 0  # 이진 탐색을 위해 a의 시작점, 끝점, 목표 페이지로 도달하는 횟수를 변수로 설정.

    while start <= end:  # start와 end가 역전될 때 탐색이 끝난다.
        middle = (start + end) // 2 # int((start + end)/2)
        
        if middle == Pa:  # 탐색할 때마다 count를 1 늘린다.
            a_count += 1
            break
        
        elif middle > Pa:
            a_count += 1
            end = middle - 1
        
        else:
            a_count += 1
            start = middle + 1

    start = 1
    end = P
    b_count = 0  # 이진 탐색을 위해 b의 시작점, 끝점, 목표 페이지로 도달하는 횟수를 변수로 설정.

    while start <= end:  # start와 end가 역전될 때 탐색이 끝난다.
        middle = (start + end) // 2
        
        if middle == Pb:  # 탐색할 때마다 count를 1 늘린다.
            b_count += 1
            break
        
        elif middle > Pb:
            b_count += 1
            end = middle -1
        
        else:
            b_count += 1
            start = middle + 1

    print(f'#{i}', end = ' ')
    
    if a_count < b_count:  # 탐색 횟수가 적은 쪽을 출력.
        print('A')
    elif a_count > b_count:
        print('B')
    else:
        print('0')