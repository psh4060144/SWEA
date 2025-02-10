# 달팽이 문제

T = int(input())

for i in range(1, T + 1):

    N = int(input())

    arr = [[0] * N for _ in range(N)]  # N * N의 0으로 된 필드 생성.

    row, col = 0, 0

    # 달팽이 숫자의 방향: 우 -> 하 -> 좌 -> 상
    row_dir = [0, 1, 0, -1]
    col_dir = [1, 0, -1, 0]

    # 오른쪽으로 이동하며 1, 2, 3, 4, 5 넣기
    num = 1
    direction = 0

    while True:                     # 1칸 이동해서 숫자 기입하는 while 문.
        arr[row][col] = num
        num += 1
        if num == N ** 2 + 1:
            break
        row = row + row_dir[direction]
        col = col + col_dir[direction]
        # 범위를 벗어나거나 숫자가 들어있다면 방향을 바꿔준다.
        if col >= N or row >= N or col < 0 or row < 0 or arr[row][col]:
            row -= row_dir[direction]
            col -= col_dir[direction]
            direction = (direction + 1) % 4
            row += row_dir[direction]
            col += col_dir[direction]

    print(f'#{i}')
    for row in range(len(arr)):
        for col in range(len(arr)):
            print(arr[row][col], end= ' ')
        print('')