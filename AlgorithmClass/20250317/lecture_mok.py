# 그럼, 정렬을 섞어서 쓰는 경우는 없나?
# 그러니까, 퀵소트로 나눠서 그걸 머지소트 한다거나, 머지소트해서 퀵소트로 마무리 한다거나 하는 일은 없나?
# 비효율적이다......

# 머지 소트: 정렬된 두 값을 정렬하는 것을 반복.
# 퀵 소트: 피봇을 중심으로 좌우를 가르는 행동을 반복.


########################################################################
# 머지 소트. but 굉장히 원시적인. 로직 자체를 이해하는 데에만 사용하자.
def old_merge(arr1, arr2):  # 정렬된 두 배열을 병합해서 반환하는 함수.
    sorted_arr = []

    while arr1 and arr2:  # 각각은 정렬되어 있으므로, 0번 index 값만 비교해서 pop 하면 로직 성립.
        if arr1[0] < arr2[0]:
            sorted_arr.append(arr1.pop(0))
        else:
            sorted_arr.append(arr2.pop(0))

    sorted_arr += arr1
    sorted_arr += arr2

    return sorted_arr


def old_merge_sort(arr):  # list 를 인자로 받아, 정렬해서 반환하는 함수.
    if len(arr) == 1:
        return arr  # 요소가 하나라면 이미 정렬된 상태이므로 본인을 반환.

    m = len(arr) // 2  # 가운데 index

    left = arr[:m]
    right = arr[m:]
    # 위 두 list 는 정렬된 상태가 아님. 즉, 정렬을 해야 함. 어떻게? 재귀 형태로.

    left = old_merge_sort(left)
    right = old_merge_sort(right)

    # 정렬된 두 list 를 병합해서 반환한다.
    sorted_arr = old_merge(left, right)
    return sorted_arr


arr = [1, 6, 2, 5, 4, 3]
print(old_merge_sort(arr))
########################################################################


########################################################################
# 머지 소트 with indexing.
def merge(start, end):
    i = start
    mid = (start + end) // 2
    j = mid + 1
    tmp_arr = []

    while i <= mid and j <= end:  # 비교할 요소가 남아 있다면 비교하기.
        if arr[i] < arr[j]:
            tmp_arr.append(arr[i])
            i += 1
        else:
            tmp_arr.append(arr[j])
            j += 1

    # 둘 중 하나는 모두 쓰고, 하나는 요소가 남는다. 따라서, 남은 요소를 붙여 준다.
    while i <= mid:
        tmp_arr.append(arr[i])
        i += 1

    while j <= end:
        tmp_arr.append(arr[j])
        j += 1

    for k in range(len(tmp_arr)):
        arr[start + k] = tmp_arr[k]
    return


def merge_sort(start, end):
    if start == end:
        return  # 요소가 하나라면(시작점과 끝점이 같다면) 이미 정렬된 상태이므로 아무것도 하지 않음..
    mid = (start + end) // 2  # 중간값.

    # 중간이 위의 예시와는 다르다. 한 칸 앞에 있다.
    # 그러므로, 오른쪽 절반에는 중간값이 들어가면 안 된다.
    merge_sort(start, mid)
    merge_sort(mid + 1, end)
    merge(start, end)


arr = [1, 6, 2, 5, 4, 3]
N = len(arr)
merge_sort(0, N - 1)
print(arr)
########################################################################
