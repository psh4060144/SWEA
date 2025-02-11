# GNS
import sys
sys.stdin = open('GNS_test_input.txt', 'r')

# 1
T = int(input())  # test case

for _ in range(1, T + 1):

    N, M = list(input().split())  # test case number, 숫자 갯수.
    M = int(M)  # 숫자 갯수 str 을 int 로 고쳐줌.

    arr = list(input().split())  # 총 test case 요소를 받음

    order = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']  # 순서를 설정
    new_order = []  # 새로 만들어 줄 list 를 제작

    for i in range(10):
        for j in range(M):
            if arr[j] == order[i]:
                new_order.append(arr[j])  # list 의 모든 요소를 보고, order 의 순서대로 하나씩 append.

    print(N)
    for i in range(M):
        print(new_order[i], end = ' ')  # 단어 하나씩 붙여서 출력.
    print('')
