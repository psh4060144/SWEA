N = 10
p = [None] * (N + 1)


def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] == x:  # 내가... 대표...?
        return x
    else:
        return find_set(p[x])


def union(x, y):
    # 한 요소의 대표자의 부모를 다른 요소 대표자로 변경.
    rx = find_set(x)
    ry = find_set(y)
    if rx >= ry:
        p[rx] = ry
    else:
        p[ry] = rx
