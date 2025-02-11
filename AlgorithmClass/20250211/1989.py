# 초심자의 회문 검사

T = int(input())  # test case

for i in range(1, T + 1):  # test case 만큼 반복.

    string = list(input())  # 들어오는 단어를 받음
    new_string = ''  # 새 단어를 만들기 위해 빈 단어를 만듦.

    for j in range(len(string)):
        new_string += string[len(string) - j - 1]  # 단어를 뒤집어서 하나씩 new_string 에 붙임.

    if ''.join(string) == new_string:  # 둘을 비교해서 같으면 1, 다르면 0 출력.
        print(f'#{i} {"1"}')
    else:
        print(f'#{i} {"0"}')
