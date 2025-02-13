# 회문 2


def solve(arr):  # arr 에서 길이 M 인 회문의 갯수를 반환하는 함수
    max_len = 1

    for row in range(N):  # 행 순회 반복문
        for M in range(N, max_len, -1):  # 회문 길이를 변화하면서 반복. 최대로 줄여볼 길이 = max_len.
            # 왜냐? 찾았던 max_len 보다 짧은 건 찾을 필요가 없기 때문에.

            find = False

            for start in range(N - M + 1):  # 회문의 시작점. start 에서 시작하는 길이 M 짜리 문자열을 검사.

                is_palindrome = True

                for col in range(M // 2):  # 회문 의심 문장 내에서 실제로 회문을 검사하는 index.
                    # start, start + M - col / start + 1, start + M - 1 - col.
                    if arr[row][start + col] != arr[row][start + M - 1 - col]:

                        is_palindrome = False
                        break

                if is_palindrome:
                    if max_len < M:
                        max_len = M

                    find = True  # 바로 다음 시작점을 찾는다.
                    break

            if find:  # 더 짧은 회문을 찾을 필요가 없다.
                break

    return max_len


T = 10

for _ in range(T):

    tc = input()
    N = int(input())
    arr = [input() for _ in range(N)]

    result = solve(arr)
    print(f'{tc} {result}')
