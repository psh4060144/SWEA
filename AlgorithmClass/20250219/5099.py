# 피자 굽기

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    input_pizza = list(map(int, input().split()))

    pizza_list = [el for el in enumerate(input_pizza, start = 1)]
    # pizza_list = []
    # for i in range(M):  # input_list = 치즈 양, i + 1 = 피자 번호
    #     pizza_list.append((input_pizza[i], i + 1))
    queue = []

    for i in range(N):  # 화덕의 크기만큼 피자 넣기
        queue.append(pizza_list[i])

    next = N  # 문제 조건에 따라 N개의 피자가 화덕에 들어감. = 다음에 들어갈 피자는 N번 피자.

    while len(queue) > 1:  # 피자가 하나 남을때까지 화덕 가동.
        num, cheese = queue.pop(0)
        cheese = cheese // 2
        if cheese == 0:  # 치즈 다 녹은 피자는 빼고 새 피자 넣기
            if next < M:  # 남아있는 피자가 있으면 넣기
                queue.append(pizza_list[next])
                next += 1
        else:  # 치즈가 덜 녹았다면
            queue.append((num, cheese))

    last_pizza = queue.pop(0)
    print(f'#{tc} {last_pizza[0]}')