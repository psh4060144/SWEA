def recur(cnt, start):
    if cnt == n:
        print(*path)
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(cnt + 1, i + 1)
        path.pop()


arr = ['A', 'B', 'C', 'D', 'E']
n = 3
path = []

recur(0, 0)
