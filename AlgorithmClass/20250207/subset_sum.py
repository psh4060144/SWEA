T = int(input())

for i in (1, T + 1):

    N, K = list(map(int, input().split()))
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    L = len(arr)
    count = [0] * 12
    sum = 0

    # 부분집합의 len이 3인 counting sort로 요소를 전부 더한다.

    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

    for el1 in range(L - 2):
        count[el1] = 1

        for el2 in range(L - el1 - 2):
            count[el1 + el2 + 1] = 1

            for el3 in range(L - el1 - el2 - 2):
                count[el1 + el2 + el3 + 2] = 1

                # for _ in range(L):

                #     sum += 






                count[el1 + el2 + el3 + 2] = 0
            
            count[el1 + el2 + 1] = 0
        
        count[el1] = 0

