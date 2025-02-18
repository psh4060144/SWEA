def calc(lst):
    stack = []
    result = None

    for token in lst:
        if token.isdecimal():
            stack.append(int(token))
        else:
            if token != '.':
                if len(stack) < 2:
                    return 'error'
                else:
                    b = stack.pop()
                    a = stack.pop()
                    if token == '+':
                        result = a + b
                    elif token == '-':
                        result = a - b
                    elif token == '*':
                        result = a * b
                    elif token == '/':
                        result = a / b
                    stack.append(result)

            else:
                if len(stack) == 1:
                    return int(stack[0])
                else:
                    return 'error'

T = int(input())

for tc in range(1, T + 1):

    lst = input().split()
    print(f'#{tc} {calc(lst)}')
