# 조합: 집합에서 원하는 갯수만큼의 요소를 뽑기.

def combi(idx, cnt):
    if cnt == K:
        print(check)
        return

    if idx == N:
        return

    check[idx] = 1
    combi(idx + 1, cnt + 1)
    check[idx] = 0
    combi(idx + 1, cnt)


arr = [1, 2, 3, 4, 5]
N = len(arr)
K = 3
check = [0] * N
combi(0, 0)
