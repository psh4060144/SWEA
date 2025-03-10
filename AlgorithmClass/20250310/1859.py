import sys
sys.stdin = open("1859_input.txt", "r")

# 백만 장자 프로젝트

T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N = int(input())  # 날짜 갯수를 받음.
    arr = list(map(int, input().split()))  # 각 날짜별 가격을 받음.
    count = 0  # 사야 하는 갯수를 세기 위해 변수를 설정.
    total = 0  # 샀을 때의 전체 가격을 알기 위해 변수를 설정.
    sumtotal = 0  # 최대 이익을 알기 위해 변수를 설정.
    N -= 1  # 1일차부터 시작하므로 indexing 을 원활하게 하기 위해 날짜에서 1을 빼 줌. 기준 날짜로 설정.
    i = N  # 날짜 역순으로 가격 확인을 하기 위해 변수를 설정.

    while i >= 0:  # 첫 날까지 확인.
        if arr[N] >= arr[i]:  # 기준 날짜의 가격이 확인하는 날짜의 가격보다 높다면
            count += 1  # 사야 하는 갯수에 추가하고
            total += arr[i]  # 샀을 때의 전체 가격에 추가하고
            i -= 1  # 그 전 날로 이동.
        else:  # 기준 날짜의 가격이 확인하는 날짜의 가격보다 낮다면
            sumtotal += (arr[N] * count) - total  # 그 때까지 확인했던 모든 날짜의 최대 이익을 추가.
            N = i  # 기준 날짜를 현재 날짜로 이동.
            count = 0  # 사야 하는 갯수 초기화.
            total = 0  # 샀을 때의 전체 가격 초기화.
    sumtotal += (arr[N] * count) - total  # 전부 확인했을 때, 마지막 확인에서 이익이 추가되지 않을 수 있으므로 추가 해 줌.

    print(f'#{tc} {sumtotal}')  # 양식에 맞게 출력.
