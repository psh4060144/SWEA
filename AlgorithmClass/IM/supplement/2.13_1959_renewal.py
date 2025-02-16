# 두 개의 숫자열

T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    N, M = list(map(int, input().split()))
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))  # 주어지는 정보들을 모두 받아옴
    mul_sum_max = 0  # 곱한 값을 모두 더한 최댓값을 구하기 위해 변수를 설정.

    if len(Ai) > len(Bj):  # 항상 더 긴 list 를 Bj 로 바꿔줌.
        Ai, Bj = Bj, Ai

    for i in range(len(Bj) - len(Ai) + 1):  # 더 짧은 쪽을 움직이며 곱할 거기 때문에 더 긴 쪽을 기준으로 함.
        mul_sum = -0xffffffff  # 대충 -42억
        
        for j in range(len(Ai)):  # 값을 곱해서 더해줌
            mul_sum += Ai[j] * Bj[j + i]
            
        if mul_sum_max < mul_sum:  # 더 큰 값을 max 로 바꿔줌.
            mul_sum_max = mul_sum

    print(f'#{tc} {mul_sum_max}')