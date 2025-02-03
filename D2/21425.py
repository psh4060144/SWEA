# +=

line_total = int(input())

for i in range(1, line_total + 1):
    input_data = list(map(int, input().split()))
    x = input_data[0]
    y = input_data[1]
    N = input_data[2]
    repeat = 0
    while x <= N:
        if x > y:
            x, y = y, x
        repeat += 1
        x += y
    print(repeat)