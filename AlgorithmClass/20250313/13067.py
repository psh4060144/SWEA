# 화물 도크

T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N = int(input())  # 화물차의 갯수를 입력.
    truck = []  # 화물차의 정보를 입력받기 위해 빈 list 를 제작.

    for _ in range(N):  # 화물차 갯수만큼 반복.
        s, e = map(int, input().split())  # 시작 시간, 종료 시간을 각각 받아
        truck.append((s, e))  # 화물차 정보에 tuple 형태로 입력.

    truck.sort(key=lambda x: x[1])  # 종료 시간을 기준으로 정렬.

    cnt = 0  # 화물차의 최대 이용 횟수를 구하기 위해 변수를 설정.
    E = 0  # 각 화물차의 종료 시간을 기준으로 하기 위해 변수를 설정.
    for i in range(N):  # 모든 화물차를 순회하면서
        if truck[i][0] >= E:  # 화물차의 시작 시간이 종료 시간보다 같거나 큰 트럭을
            cnt += 1  # 카운팅 한 후
            E = truck[i][1]  # 종료 시간을 새 기준으로 설정.

    print(f'#{tc} {cnt}')  # 화물차 갯수를 출력.
