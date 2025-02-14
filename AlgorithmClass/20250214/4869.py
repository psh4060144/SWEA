# 종이붙이기


def f(num):  # 함수를 제작
    global memo  # memoization 사용
    if num > 2 and memo[num] == 0:  # f(1), f(2)를 구한 뒤, 그 이후만 계산.
        memo[num] = f(num - 1) + f(num - 2) * 2  # memoization 된 전 값과 전전 값을 이용해 해당 index 에 memoization 해줌.
    return memo[num]  # return 값을 설정해야 line 7 에서 오류가 나지 않는다.


T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    num = int(input()) // 10  # 10의 자리는 떼고 생각. 기니까...
    memo = [0] * (num + 1)  # 인수 갯수 + 1 만큼 memoization 공간을 생성해야 해당 인수를 index 로 하는 공간에 값을 넣을 수 있다.
    memo[1] = 1
    memo[2] = 3  # f(1), f(2) 값을 입력.
    f(num)  # 함수 실행

    print(f'#{tc} {memo[num]}')
