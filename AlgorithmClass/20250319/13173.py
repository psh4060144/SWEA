# 연산
# 원형 queue......


def enqueue(data):  # 원형 queue 에 값을 입력하는 함수.
    global rear  # rear 전역 변수 설정.
    rear = (rear + 1) % 1000000  # rear 한 칸 이동.
    queue[rear] = data  # 이동한 자리에 data 입력.


def dequeue():  # 원형 queue 의 값을 꺼내는 함수.
    global front  # front 전역 변수 설정.
    front = (front + 1) % 1000000  # rear 한 칸 이동.
    return queue[front]  # 이동한 자리의 data 출력.


def bfs(start):  # 연산 횟수를 반환하는 함수.

    enqueue((start, 0))  # 초기값 원형 queue 에 입력.
    check = [0] * 1000001  # 사용한 값인지 확인하기 위해 list 설정.

    while True:  # 연산을 수행.
        current, cnt = dequeue()  # 원형 queue 에서 숫자를 뽑아 옴.

        if current < 0 or current > 1000000 or check[current]:  # 유효 범위 밖이거나 사용한 값이라면
            continue  # 다음 숫자 뽑아오기.

        if current == M:  # 현재 숫자가 목표 숫자와 같다면
            return cnt  # 연산 횟수를 반환.

        check[current] = 1  # 숫자에 사용 표시.
        enqueue((current + 1, cnt + 1))
        enqueue((current - 1, cnt + 1))
        enqueue((current * 2, cnt + 1))
        enqueue((current - 10, cnt + 1))  # 사용할 수 있는 연산을 모두 수행.


T = int(input())  # test case
for tc in range(1, T + 1):  # test case 만큼 반복.

    N, M = map(int, input().split())  # 시작 숫자 N, 목표 숫자 M 입력.
    queue = [None] * 1000000  # 원형 queue 를 만들기 위해 긴 list 제작.
    front, rear = 1, 1  # front, rear 의 초기값 설정.
    result = bfs(N)  # 연산 횟수를 반환하는 함수 실행.

    print(f'#{tc} {result}')  # 양식에 맞게 출력.
