# 1 대 1 가위바위보

InputData = input()
a, b = InputData.split()

if a == b:
    print('무승부?!')
elif a > b:
    if a == '3' and b == '1':
        print('B')
    else:
        print('A')
else:
    if a == '1' and b == '3':
        print('A')
    else:
        print('B')