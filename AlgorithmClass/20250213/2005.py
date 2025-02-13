# 파스칼의 삼각형

# idea
# 그 다음 행을 만들기 위해서는 그 전 행과 그 전 행을 한 칸 들여쓴 행을 서로 더해야 한다.
# 예를 들어, [1 3 3 1] 의 다음 행을 구하기 위해서는 [0 1 3 3 1] 과 [1 3 3 1 0] 을 같은 index 끼리 더해야 한다.


def f(num):  # 파스칼의 삼각형 각 행을 만드는 함수
    if num == 1:  # 제일 첫 행은 1
        return [1]
    a = b = f(num - 1)  # 특정 행을 만들기 위해 그 전 행을 두 가지 변수에 설정
    a = [0, *a]  # 하나는 앞에 0을 넣고
    b = [*b, 0]  # 하나는 뒤에 0을 넣음
    c = []  # 행의 인수를 담기 위해 빈 list 를 만듦
    for i in range(len(a)):  # 각 index 끼리 더해서
        c.append(a[i] + b[i])  # 더한 값을 c 에 차례대로 넣는다.
    return c  # c 를 반환


T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    num = int(input())  # 파스칼의 삼각형 행 수를 받음

    print(f'#{tc}')
    for i in range(1, num + 1):  # 각 행을 만드는 함수를 매 행마다 반복하면
        print(*f(i))  # 파스칼의 삼각형을 얻을 수 있다