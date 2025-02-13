# 회문 1


def solve(arr):  # arr 에서 길이 M 인 회문의 갯수를 반환하는 함수
    result = 0

    for row in range(N):  # 행 순회 반복문
        for start in range(N - M + 1):  # 회문의 시작점. start 에서 시작하는 길이 M 짜리 문자열을 검사.
            flag = True

            for col in range(M // 2):  # 회문 의심 문장 내에서 실제로 회문을 검사하는 index.
                # start, start + M - col / start + 1, start + M - 1 - col.
                if arr[row][start + col] != arr[row][start + M - 1 - col]:
                    flag = False
                    break

            if flag:
                result += 1

    return result


T = 10

for tc in range(1, T + 1):

    N = 8
    M = int(input())

    arr = [input() for _ in range(N)]
    result = solve(arr)
    print(result)
