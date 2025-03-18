################################################################
# 퀵 소트 but 매우 원시적인. logic 자체를 이해하는 용도로만 사용.
def old_partition():
    pass


# 정렬 대상 배열을 pivot 기준으로 작은 값 / 큰 값으로 나누기.
# 나뉜 값이 정렬된 게 아니기 때문에, 나뉜 값을 다시 정렬.
# 인자로 받은 arr 배열을 정렬해서 반환하는 함수
def old_quick_sort(arr):
    if len(arr) < 2:  # merge sort 와 조건이 다른 이유: merge sort 는 반드시 양쪽이 있지만, quick sort 는 없는 경우도 있다.
        return arr

    # 파티션: pivot 을 기준으로 큰 값과 작은 값으로 일단 나눈다. 정렬은 아직 안 함.
    # pivot 은 아무거나 잡으면 된다. 첫 번째 요소로 잡는 게 일반적.
    pivot = arr(0)
    small = []  # pivot 보다 작은 값을 모으는 배열
    big = []  # pivot 보다 큰 값을 모으는 배열

    # pivot 으로 잡은 첫 번째 요소는 제외하고 그 다음부터 검사.
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            small.append(arr[i])
        else:
            big.append(arr[i])

    # small, big 은 정렬된 상태가 아님. 즉, 재귀 호출을 통해 정렬해주어야 함.
    small = old_quick_sort(small)
    big = old_quick_sort(big)

    sorted_arr = small + [pivot] + big
    return sorted_arr


arr = [5, 6, 7, 3, 4, 2, 1, 8, 9]
print(old_quick_sort(arr))
################################################################


################################################################
# quick sort with indexing.

# 시작점과 종료점 내에서 pivot 을 기준으로 큰 값과 작은 값으로 나누고, pivot 의 위치를 반환하는 함수.
def partition(start, end):  # hoare partition
    # 제일 앞 요소를 pivot_item 으로 설정.
    pivot = arr[start]

    # i: 왼쪽 끝에서 오른쪽으로 이동하며 pivot 보다 큰 값 찾기.
    # j: 오른쪽 끝에서 왼쪽으로 이동하면 pivot 보다 작은 값 찾기.
    i = start + 1
    j = end
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1  # 오른쪽으로 이동하면서 pivot 보다 큰 값 search.
        while i <= j and arr[j] >= pivot:
            j -= 1  # 왼쪽으로 이동하면서 pivot 보다 작은 값 search.
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]  # i 가 j 보다 작을 때만 위치 교환.

    # pivot 자리 찾아주기.
    arr[j], arr[start] = arr[start], arr[j]

    return j


def quick_sort(start, end):
    if start >= end:  # 범위의 역전이 생긴다면 정렬할 요소가 없는 것.
        return
    pivot = partition(start, end)  # partitioning 을 통해 pivot 을 설정.
    quick_sort(start, pivot - 1)  # 작은 쪽 정렬
    quick_sort(pivot + 1, end)  # 큰 쪽 정렬

    pass


arr = [5, 6, 7, 3, 4, 2, 1, 8, 9]
N = len(arr)
quick_sort(0, N - 1)
print(arr)
################################################################








