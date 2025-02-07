T = 1

for i in range(1, T + 1):
    
    testcase = int(input())

    matrix = [list(map(int, input().split())) for _ in range(100)]

    sum = 0
    tmp = 0

    # row_sum
    for row in range(100):
        for col in range(100):
            tmp += matrix[row][col]
            if sum < tmp:
                sum = tmp
            tmp = 0

    # col_sum
    for row in range(100):
        for col in range(100):
            tmp += matrix[col][row]
            if sum < tmp:
                sum = tmp
            tmp = 0

    # leftdown_sum
    for row in range(100):
        tmp += matrix[row][row]
        if sum < tmp:
            sum = tmp
        tmp = 0

    # rightdown_sum
    for row in range(100):
        tmp += matrix[row][99 - row]
        if sum < tmp:
            sum = tmp
        tmp = 0

    print(sum)