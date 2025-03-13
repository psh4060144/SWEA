def change(cnt):
    global max_v
    if cnt == n:
        if num not in lst:
            lst[cnt].append(list(num))
            v = 0
            for i in range(len(num)):
                v += num[i] * 10 ** (len(num) - 1 - i)
            if v >= max_v:
                max_v = v
        return

    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]
            if num in lst[cnt]:
                num[i], num[j] = num[j], num[i]
                continue
            else:
                lst[cnt].append(list(num))
            change(cnt + 1)
            num[i], num[j] = num[j], num[i]


T = int(input())
for t in range(T):
    num, n = input().split()
    num = list(map(int, num.strip()))
    n = int(n)
    lst = [[] for _ in range(n + 1)]
    values = []
    max_v = 0
    change(0)
    print(f'#{t + 1} {max_v}')
