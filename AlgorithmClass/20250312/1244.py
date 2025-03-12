# 최대 상금


def subset(x):
    for i in range(x):
        for j in range(x):
            if i < j:
                select.append([i, j])


def test(x):
    aa = [i for i in a]
    text = ''
    for i, j in select:
        if int(aa[i]) < int(aa[j]):
            aa[i], aa[j] = aa[j], aa[i]
        else:
            continue
        for k in aa:
            text += k
        if int(text) > A:
            return text


# T = int(input())
# for tc in range(1, T + 1):

A, b = list(map(int, input().split()))
a = list(str(A))

select = []

subset(len(a))
# test(1)

print(select)


