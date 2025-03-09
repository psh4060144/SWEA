# 증가하는 사탕 수열


def solve(lst):  # 먹을 사탕의 갯수를 반환하는 함수
    if lst[2] < 3:  # 마지막 숫자가 3 이상이 아니라면 수열을 만들 수 없다.
        return -1  # 따라서, -1을 반환.

    count = 0  # 먹을 사탕의 갯수를 세기 위해 변수 설정.
    for i in range(2, 0, -1):  # 뒤쪽부터 거꾸로 탐색. 두 번만 반복.
        if lst[i] <= lst[i - 1]:  # 만약 어떤 박스가 그 전 박스보다 사탕이 적거나 같다면
            tmp = lst[i - 1] - lst[i] + 1  # 그 전 박스에서 먹어야 하는 사탕 갯수를 설정.
            count += tmp  # 먹어야 하는 사탕 갯수를 추가하고,
            lst[i - 1] -= tmp  # 그 전 박스에서 사탕을 제거.
        if lst[i - 1] == 0:  # 빈 사탕 박스가 생긴다면
            return -1  # 마찬가지로 불가능하므로 -1을 반환.

    return count  # 사탕 갯수를 반환.


T = int(input())  # test case
for tc in range(1, T + 1):  # test case 만큼 반복

    lst = list(map(int, input().split()))  # 사탕 박스 list 를 입력
    result = solve(lst)  # 먹을 사탕의 갯수를 반환하는 함수 실행
    print(f'#{tc} {result}')  # 양식에 맞게 출력
