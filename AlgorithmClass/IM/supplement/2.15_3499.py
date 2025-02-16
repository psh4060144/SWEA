# 퍼펙트 셔플

T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    N = int(input())  # 카드 장수 입력

    deck = list(input().split())  # 카드 이름 입력

    n1 = deck[:(N // 2) + (N % 2)]
    n2 = deck[(N // 2) + (N % 2):]  # 카드를 절반 만큼 slicing 하는데, 홀수라면 n1 이 n2 보다 한 장 많게 slicing 한다.


    print(f'#{tc}', end=' ')  # test case 번호 출력
    for i in range(len(n1)):  # 출력할 때 교대로 출력하는데, 
        print(n1[i], end=' ')
        if i == len(n2):  # n2 가 n1 보다 한 장 적으니 그 때 indexing 을 하지 않도록 해 준다.
            pass
        else: print(n2[i], end=' ')
    print()