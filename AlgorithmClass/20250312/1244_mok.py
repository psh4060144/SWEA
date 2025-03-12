arr = [1, 2, 3]
N = len(arr)
k = 3


def change(idx):
    if idx == k:
        print(arr)
        return
    for i in range(N):
        for j in range(i + 1, N):
            arr[i], arr[j] = arr[j], arr[i]
            change(idx + 1)
            arr[i], arr[j] = arr[j], arr[i]


change(0)
