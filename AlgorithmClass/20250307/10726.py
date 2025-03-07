import sys
sys.stdin = open('10726_input.txt', 'r')


def solve():
    target = M
    for _ in range(N):  # 연속된 N 개의 숫자를 확인
        if target & 0x1 == 0:  # 맨 우측 bit 가 1인지 체크. 0x1 로 표시하는 이유: bit 연산을 표시하기 위해.
            return 'OFF'
        target == target >> 1  # 맨 우측 bit 를 삭제
    return 'ON'


# 더 단순한 방법
def solve2():
    mask = (1 << N) - 1  # N 개의 1 을 구함.
    result = (M & mask) == mask
    if result:
        return 'ON'
    else:
        return 'OFF'

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = solve()
    result2 = solve2()
    print(f'#{tc} {result}')
    print(f'#{tc} {result2}')