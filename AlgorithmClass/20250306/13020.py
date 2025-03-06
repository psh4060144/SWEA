# 이진수 2

def binary(num):  # 소수점 이진수를 만드는 함수
    full = []  # 이진수 값을 담기 위해 빈 list 를 만듦.
    count = 0  # 이진수 계산 및 overflow 판별을 위해 변수를 설정

    while num:  # 0이 아닐때까지 반복. 0이 되면 멈춤.
        if count < 13:  # overflow 가 되는 수가 아닐때까지 반복.
            count += 1  # 이진수 계산용 지수를 늘려줌.
            if num >= 1 / (2 ** count):  # 이진수 계산용 숫자보다 입력값이 더 크다면
                full.append(1)  # 이진수 값에 1을 추가하고
                num -= (1 / (2 ** count))  # 숫자에서 이진수 계산용 숫자를 빼 줌.
            else:  # 이진수 계산용 숫자보다 입력값이 더 작다면
                full.append(0)  # 이진수 값에 0을 추가하고, 숫자를 빼 줄 이유는 없음.
        else:  # overflow 가 된다면
            return 'overflow'  # overflow 반환.
    return full  # while 문이 정상적으로 종료되면 만들어진 이진수 값 반환.


T = int(input())  # test case
for tc in range(1, T + 1):  # test case 만큼 반복

    num = float(input())  # 인수를 받을 때, 실수로 받아야 함.
    result = binary(num)  # 소수점 이진수 함수 실행

    print(f'#{tc}', end=' ')  # 양식에 맞게 출력
    if type(result) == list:  # 이진수 값이 반환되었다면
        for i in range(len(result)):
            print(result[i], end='')  # 이진수를 붙여 출력
    else:  # overflow 가 반환되었다면
        print(result, end='')  # 그대로 출력
    print()