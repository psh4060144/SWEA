def merge(start, end):
    global count
    mid = (start + end) // 2
    i = start
    j = mid + 1
    tmp_arr = []

    if arr[mid] > arr[end]:  # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 count 에 1 추가.
        count += 1

    while i <= mid and j <= end:  # 왼쪽과 오른쪽을 처음부터 비교해서 작은 값 붙이기.
        if arr[i] < arr[j]:
            tmp_arr.append(arr[i])
            i += 1
        else:
            tmp_arr.append(arr[j])
            j += 1
    # 위 while 문을 끝내면 왼쪽, 오른쪽 중 하나는 요소를 다 쓴다.

    # 남은 요소를 모두 붙여주면 병합 끝.
    while i <= mid:
        tmp_arr.append(arr[i])
        i += 1

    while j <= end:
        tmp_arr.append(arr[j])
        j += 1

    # tmp_arr 의 제작이 끝났으므로, 기존 list 와 바꿔준다.
    for k in range(len(tmp_arr)):
        arr[start + k] = tmp_arr[k]

    return


def merge_sort(start, end):
    if start == end:  # 요소가 하나라면
        return  # 아무 것도 하지 않는다.

    mid = (start + end) // 2  # 중간 index 찾기.
    merge_sort(start, mid)  # 시작점부터 중간점까지 merge_sort 실행.
    merge_sort(mid + 1, end)  # 중간점 다음부터 끝점까지 merge_sort 실행.
    merge(start, end)  # 시작점부터 끝점까지 병합.


T = int(input())
for tc in range(1, T + 1):

    N = int(input())
    arr = list(map(int, input().split()))
    count = 0

    merge_sort(0, N - 1)
    print(arr, count)