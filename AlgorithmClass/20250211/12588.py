# 문자열 비교

T = int(input())  # test case

for i in range(1, T + 1):  # test case 수만큼 반복

    str1 = input()  # 단어 1을 받음
    str2 = input()  # 단어 2를 받음

    new_str = str2.split(str1)  # 단어 2를 단어 1을 단위로 split. 이를 통해 (단어 포함 갯수 + 1) 만큼의 길이의 list 가 생성됨.

    print(f'#{i} {len(new_str) - 1}')  # list 길이 - 1 = 단어 포함 갯수
