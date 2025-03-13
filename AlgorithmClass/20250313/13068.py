# 베이비진 게임


def find(lst):  # 베이비진을 판별하는 함수
    for k in range(10):  # list 를 순회하면서
        if k < 8:  # 먼저 연속하는 3개의 숫자가 나오는지 판별. list 범위 안에 있고
            if lst[k] > 0 and lst[k + 1] > 0 and lst[k + 2] > 0:  # 연속하는 3개의 숫자가 나온다면
                return 1  # 1을 반환.
        if lst[k] == 3:  # 연속하는 3개의 숫자는 없지만 해당 숫자가 3개 있다면
            return 1  # 1을 반환.
    return 0  # 둘 다 없다면 0을 반환.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    cards = list(map(int, input().split()))  # 카드 list 를 입력.
    p1_lst = [0] * 10
    p2_lst = [0] * 10  # 카드 번호를 입력할 list 를 제작.
    p1_result = 0
    p2_result = 0  # 베이비진 판별 값을 받을 변수를 설정.

    for i in range(12):  # 카드를 나눠받는데
        if (i + 1) % 2 == 1:  # 홀수 번 카드라면
            p1_lst[cards[i]] += 1  # 1번 플레이어에게 주고, 카드 번호를 입력.
            p1_result = find(p1_lst)  # 베이비진 판별.
        else:  # 짝수 번 카드라면
            p2_lst[cards[i]] += 1  # 2번 플레이어에게 주고, 카드 번호를 입력.
            p2_result = find(p2_lst)  # 베이비진 판별.

        if p1_result:  # 1번 플레이어가 베이비진이라면
            print(f'#{tc} 1')  # 1번 플레이어 출력 후
            break  # 종료
        elif p2_result:  # 2번 플레이어가 베이비진이라면
            print(f'#{tc} 2')  # 2번 플레이어 출력 후
            break  # 종료.
    else:  # 둘 다 베이비진이 아니라면
        print(f'#{tc} 0')  # 무승부 출력.
