# 최대 상금


def solve(cnt):  # 최대 상금을 출력하는 함수
    global answer  # 전역 변수를 설정하여 최대 상금을 구함.
    global lst  # 전역 변수를 설정하여 각 재귀 호출마다의 결과를 저장.

    if cnt == N:  # 교환 횟수를 모두 썼다면
        for ii in range(len(lst[cnt - 1])):  # 마지막 재귀 호출 결과를 순회.
            result = 0  # 상금을 계산하기 위해 변수를 설정.
            for jj in range(L):  # 각 결과마다
                result += lst[cnt - 1][ii][jj] * 10 ** (L - jj - 1)  # 상금을 계산.
            if answer < result:  # 최대 상금보다 더 크다면
                answer = result  # 최대 상금을 갱신.
        return  # 이후 함수를 종료.

    for i in range(L - 1):  # 첫 번째 카드를 고름.
        for j in range(1, L):  # 두 번째 카드를 고름.
            if i >= j:  # 카드를 고를 때의 중복을 제거.
                continue
            num[i], num[j] = num[j], num[i]  # 두 카드의 위치를 교환.
            if num not in lst[cnt]:  # 해당 재귀 호출 결과에 포함되어 있지 않다면
                numcopy = [k for k in num]  # 깊은 복사를 하여
                lst[cnt].append(numcopy)  # 재귀 호출 결과 list 에 추가.
                solve(cnt + 1)  # 이후 다음 재귀 호출 실행.
            num[i], num[j] = num[j], num[i]  # 재귀 호출이 끝났다면 교환했던 카드의 위치를 재교환.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.
    a, N = list(map(int, input().split()))  # 숫자와 교환 횟수 입력.
    num = list(map(int, list(str(a))))  # 숫자는 list 로 바꿔줌.
    L = len(num)  # 숫자의 길이를 구함.
    answer = 0  # 최대 상금을 구하기 위해 변수를 설정.
    lst = [[] for _ in range(N)]  # 각 재귀 호출 결과를 담기 위해 빈 2차원 list 를 설정.

    solve(0)  # 최대 상금을 구하는 함수 실행.

    print(f'#{tc} {answer}')  # 양식에 맞게 출력.
