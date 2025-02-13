# 괄호 검사

T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    arr = list(map(str, input()))  # 한 줄을 받음

    stack = [None] * len(arr)  # stack 을 만들어 주고, top 값을 설정.
    top = -1

    for char in range(len(arr)):  # 모든 문자를 봐 가면서
        flag = True  # 가장 바깥의 for 문을 break 하기 위해 flag를 추가.
        if arr[char] == '(' or arr[char] == '{':  # 여는 괄호는 stacking.
            top += 1
            stack[char] = arr[char]

        if arr[char] == ')':  # 닫는 소괄호를 만났을 때
            for i in range(char - 1, -1, -1):  # 거기부터 거꾸로 탐색하면서
                if stack[i] == '{':  # 중괄호를 만난다면 break.
                    flag = False  # flag 를 False 로 바꿈.
                    break
                elif stack[i] == '(':  # 소괄호를 만난다면 제거하고 break.
                    top -= 1
                    stack[i] = None
                    break
            else:  # 괄호를 만나지 못했다면
                top = 0xffffffff  # top 을 매우 크게
                break

        if arr[char] == '}':  # 닫는 중괄호를 만났을 때
            for i in range(char - 1, -1, -1):  # 거기부터 거꾸로 탐색하면서
                if stack[i] == '(':  # 소괄호를 만난다면 break.
                    flag = False  # flag 를 False 로 바꿈.
                    break
                elif stack[i] == '{':  # 중괄호를 만난다면 제거하고 break.
                    top -= 1
                    stack[i] = None
                    break
            else:  # 괄호를 만나지 못했다면
                top = 0xffffffff  # top 을 매우 크게
                break

        if not flag:  # flag 가 False 라면 괄호에 문제가 있는 것. 즉시 종료.
            break

    if top == -1:  # top 값이 초기값으로 돌아와야 괄호가 완전한 것.
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')