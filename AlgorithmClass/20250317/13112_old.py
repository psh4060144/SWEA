def merge_sort(arr):  # slicing 을 이용한 merge sort 함수.
    N = len(arr)  # list 의 길이를 측정.

    if N == 1:  # 길이가 1이라면
        return arr  # 그 값 그대로 반환.

    left = arr[0 : N // 2]
    right = arr[N // 2 : N]  # 문제에서 제시한 대로 범위를 잡아 줌.

    left = merge_sort(left)
    right = merge_sort(right)  # 좌, 우에서 각각 재귀 호출. 이를 통해 가장 아랫단에서부터 올라오면서 정렬을 수행함.

    sorted_arr = merge(left, right)  # 병합 함수 실행.

    return sorted_arr  # 병합된 list 를 반환.


def merge(arr1, arr2):  # 병함 함수.
    global count  # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력하기 위해 전역 변수를 설정.
    sorted_arr = []  # 병합한 list 를 만들기 위해 빈 list 를 제작.

    if arr1[-1] > arr2[-1]:  # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 크다면
        count += 1  # count 에 1 추가.

    i = 0
    j = 0  # indexing 을 위해 변수를 설정.

    while i < len(arr1) and j < len(arr2):  # slicing 된 list 를 순회하면서 i 와 j 가 각각의 list 내에 있을 때만 반복.
        # 두 list 를 앞에서부터 비교하여 더 작은 값을 sorted_arr 에 추가.
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
        # while 문이 끝나면 반드시 모두 사용한 list 가 하나는 존재.

    # 따라서, 덜 사용한 list 부분을 sorted_arr 뒤에 추가.
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    return sorted_arr  # 정렬된 list 를 반환.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N = int(input())  # 정수의 갯수를 입력.
    arr = list(map(int, input().split()))  # 정수 list 를 입력.
    count = 0  # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력하기 위해 변수를 설정.
    result = merge_sort(arr)  # slicing 을 이용한 merge sort 함수 실행.
    print(f'#{tc} {result[N // 2]} {count}')  # 양식에 맞게 출력.
