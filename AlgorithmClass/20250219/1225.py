# 암호생성기

T = 10  # test case

for _ in range(T):  # test case 만큼 반복.

    tc = int(input())  # test case 번호를 받음
    data = list(map(int, input().split()))  # 숫자열 list 를 받음
    end = 1  # while 문을 돌리기 위해 0이 아닌 변수를 설정.

    while end != 0:  # 마지막 수가 0이 아닐 때까지 반복.
        end = data[-1]  # while 문의 조건을 list 의 마지막 수로 변경.

        for i in range(1, 6):  # cycle 을 돌기 위해 for 문을 설정.
            if data[-1] == 0:  # 마지막 수가 0이라면 cycle 을 더 돌지 않고 종료.
                break

            tmp_data = data.pop(0) - i  # 제일 앞 수를 뽑아서 cycle 을 돌아줌.

            if tmp_data <= 0:  # cycle 을 돌았을 때 마지막 수가 0 이하라면 0으로 처리.
                tmp_data = 0

            data.append(tmp_data)  # 마지막에 붙여줌.

    print(f'#{tc}', end=' ')
    print(*data)  # 출력.