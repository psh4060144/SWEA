# 요리사

# idea
# N // 2 개의 식재료 부분집합을 구할 때, 첫 번째 식재료를 고정하고 나머지 식재료의 모든 부분집합을 구하면 중복 없이 구할 수 있다.


def origin(cnt, start):  # 부분집합을 구하는 함수.

    if cnt == N // 2:  # 부분집합의 길이가 N // 2 일 경우, 즉 요리 재료를 절반씩 나눈 경우
        if path[0] == 0:  # 첫 식재료를 쓴 경우에만
            subset.append(tuple(path))  # 부분집합에 tuple 형식으로 추가해 준다.
        return  # 이후 종료.

    for i in range(start, N):  # 첫 식재료에서 끝 식재료까지 돌면서
        path.append(i)  # 재료를 추가하고
        origin(cnt + 1, i + 1)  # 다음 재료를 확인하는 작업을 반복.
        path.pop()  # 부분집합을 만들었다면 다음 재료로.


def deli():  # 가장 적은 맛 편차를 구하는 함수.
    global min_deli  # 가장 적은 맛 편차를 구하기 위해 전역 변수를 설정.

    for i in range(len(subset)):  # 모든 부분집합을 보면서

        delicious = 0  # 부분집합 하나의 맛 편차를 구하기 위해 변수를 설정.
        set_A = subset[i]  # A 음식 세트를 설정.
        set_B = list(set(range(N)) - set(subset[i]))  # B 음식 세트를 설정.
        for j in range(N // 2 - 1):  # 재료 두 개를 선정해야 하므로
            for k in range(j + 1, N // 2):  # for 문을 2번 돌면 된다.
                delicious += field[set_A[j]][set_A[k]] + field[set_A[k]][set_A[j]]  # A 음식 세트의 총 맛 점수를 더해주고,
                delicious -= field[set_B[j]][set_B[k]] + field[set_B[k]][set_B[j]]  # B 음식 세트의 총 맛 점수를 빼 준다.

        if min_deli > abs(delicious):  # 항상 A 점수를 더하고, B 점수를 빼 주면 일관적인 점수 체계가 완성되므로
            min_deli = abs(delicious)  # 그 값의 절댓값을 비교해주면 된다.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N = int(input())  # 재료 갯수를 입력.
    field = [list(map(int, input().split())) for _ in range(N)]  # 모든 조합의 맛 점수를 입력.
    subset = []  # 만들어진 부분집합을 담기 위해 빈 list 설정.
    path = []  # 부분집합을 만들기 위해 빈 list 설정.
    min_deli = 0xffffffff  # 가장 적은 맛 편차를 구하기 위해 큰 변수를 설정.
    origin(0, 0)  # 부분집합을 구하는 함수 실행.
    deli()  # 가장 적은 맛 편차를 구하는 함수 실행.
    print(f'#{tc} {min_deli}')  # 양식에 맞게 출력
