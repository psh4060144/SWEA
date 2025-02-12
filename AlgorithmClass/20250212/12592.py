# 글자 수

T = int(input())  # test case

for i in range(1, T + 1):  # test case 만큼 반복

    alphadict = {}  # 빈 dictionary 를 생성
    max_num = 0  # 최대 갯수를 찾기 위해 변수를 생성

    str1 = input()
    str2 = input()  # str1, str2 에 문자열을 그대로 받음

    for j in str1:  # str1 을 먼저 검사해서,
        alphadict[j] = 0  # 들어있는 alphabet 을 dictionary 의 key 로, value 는 나중에 갯수를 더해주기 위해 0으로 설정.

    for k in str2:  # str2 를 검사해서,
        for key in alphadict:
            if k == key:
                alphadict[key] += 1  # alphabet 이 있으면 dictionary 의 해당 alphabet key 의 value 값에 1씩 더해줌.

    for key in alphadict:
        if max_num < alphadict[key]:  # 최대 value 값을 찾아줌
            max_num = alphadict[key]

    print(f'#{i} {max_num}')