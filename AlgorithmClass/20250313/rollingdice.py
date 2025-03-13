arr = [1, 2, 3, 4, 5, 6]
n = 3
path = []


def recur(start, cnt):
    if cnt == n:
        print(*path)
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(i, cnt + 1)
        path.pop()
    print('===============')


recur(0, 0)