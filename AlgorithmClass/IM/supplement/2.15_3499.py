# 퍼펙트 셔플

T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    N = int(input())  # 카드 장수 입력

    deck = list(input().split())  # 카드 이름 입력

    n1 = deck[:(N // 2) + (N % 2)]
    n2 = deck[(N // 2) + (N % 2):]  # 카드를 절반 만큼 slicing 하는데, 홀수라면 n1 이 n2 보다 한 장 많게 slicing 한다.
    # 얕은 복사 주의!!!!!!!!!!!! 이건 깊은 복사이긴 함... 근데 메모리 더 많이 씀.
    # 이 문제의 경우 indexing 이 매우 간단하므로 slicing 하는 건 문제가 있음.


    print(f'#{tc}', end=' ')  # test case 번호 출력
    for i in range(len(n1)):  # 출력할 때 교대로 출력하는데, 
        print(n1[i], end=' ')
        if i == len(n2):  # n2 가 n1 보다 한 장 적으니 그 때 indexing 을 하지 않도록 해 준다.
            pass
        else: print(n2[i], end=' ')
    print()



#############################################################################################################

T = int(input())

for tc in range(1, T + 1):
    
    N = int(input())
    
    deck = input().split()  # 이러면 잘 받아진다
    
    left_idx = 0
    right_idx = N // 2 if N % 2 == 0 else N // 2 + 1  # 삼항 연산자
    
    print(f'#{tc}', end=' ')
    for i in range(N):
        index = left_idx + i//2 if i % 2 == 0 else right_idx + i//2
        print(deck[index], end=' ')
    print()