arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)


##############################################################
# mine


def solve(x):
    global count

    lst = []
    for i in range(n):
        if x & 0x1:
            lst.append(arr[i])
        x >>= 1
    if len(lst) < 2:
        return
    else:
        count += 1
        return


count = 0
for tar in range(0, 1 << n):
    solve(tar)
print(count)


##############################################################
# keum


def get_count(tar):
    cnt = 0
    for _ in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1
    return cnt


answer = 0
for target in range(1 << n):
    if get_count(target) >= 2:
        answer += 1
print(answer)
