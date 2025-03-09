# 배열 최소 합

def solve(row, tmp_sum):  # row 행에서 숫자 하나 고름.
    global min_v
    if tmp_sum >= min_v:  # 모든 행을 찾지 못했는데도 이미 min_v 보다 큰 값이 나온다면, 이 예시는 당연히 틀린 것.
        return  # line 5 ~ line 6 : backtracking
    if row == N:  # 모든 행에서 숫자 하나씩을 선택한 상황.
        if tmp_sum < min_v:  # 더 이상 선택할 행이 없으므로 min_v 에 tmp_sum 을 반영하고 종료.
            min_v = tmp_sum
        return
    for i in range(N):
        # arr[row][i]  # row 행의 i 번 index 에 있는 원소 하나.
        if not used[i]:  # 이전 행에서 사용했던 열은 사용하지 않도록 한다.
            used[i] = 1  # 사용했다고 표시하고
            solve(row + 1, tmp_sum + arr[row][i])  # 재귀로 다시 실행
            used[i] = 0  # 그 실행이 끝나면 표시를 지워줌.

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # (완전탐색) 각 행마다 모든 열을 선택하고, 그 중에 제일 작은 것 고르기
    min_v = 0xffffffff  # 최댓값은 정해져 있긴 하지만, 모르겠고 그냥 때려넣으면 됨.

    # 같은 열의 값을 선택하지 못하도록 사용 표시를 해 주는 배열
    used = [0] * N  # 1이면 사용했다는 뜻.
    solve(0, 0)
    print(f'#{tc} {min_v}')