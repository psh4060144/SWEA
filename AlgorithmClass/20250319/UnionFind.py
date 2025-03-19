# 서로소 집합 (상호배타 집합)
# 서로 중복 포함된 원소가 없는 집합. 즉, 교집합이 없는 집합.
# 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분. 이럴 때, 이 특정 멤버를 대표자 라고 부름.

# 상호배타 집합 연산
# Make-set(x), Find-set(x), Union(x, y)


def make_set(x):
    parents = [i for i in range(N+1)]
    return parents


def find_set(x):
    if parents[x] == x:
        return x
    return find_set(parents[x])


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    # 문제에 따라 우선되는 집합으로 합쳐주면 됨. 아래 if 문 수정.
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


N = 6
parents = make_set(N)
print(parents)

union(1, 3)
union(2, 3)
union(5, 6)
print(parents)

if find_set(3) == find_set(5):
    print('same')
else:
    print('different')

