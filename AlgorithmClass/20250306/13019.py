# 이진수

T = int(input())  # test case
for tc in range(1, T + 1):  # test case 만큼 반복

    N, num = input().split()  # 자릿수 N, 16진수를 입력.
    dictionary = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}  # 16진수의 각 알파벳에 값을 할당.
    full = []  # 이진수로 만들어줄 빈 list 를 만듦.

    for i in num:  # 모든 16진수의 자릿수에 대해
        if i.isdecimal():  # 숫자라면
            k = int(i)  # 숫자로 만들어서 k 에 대입.
        else:  # 문자라면(알파벳이라면)
            k = dictionary[i]  # dictionary 에서 value 를 불러와서 k 에 대입.

        line = []  # 각 숫자마다 이진수로 만들어서 합쳐주기 위해 빈 list 를 제작.
        for _ in range(4):  # 16진수를 이진수로 만들면 숫자 하나 당 4자리로 바뀜. 4회 반복하면 됨.
            line.append(k % 2)  # 나눈 나머지를 list 에 추가.
            k = k // 2  # 나눈 몫을 새로운 k 로 할당.

        line.reverse()  # line 이 뒤집어져서 붙기 때문에 다시 뒤집어주고
        full.extend(line)  # 이진수 list 에 추가.

    print(f'#{tc} ', end='')  # 양식에 맞게 출력
    for i in range(int(N) * 4):  # N 이 문자이기 때문에 숫자로 바꿔서 반복
        print(full[i], end='')
    print()