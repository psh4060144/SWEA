N = int(input())  # 숫자 입력
for i in range(1, N + 1):  # 1부터 숫자 까지
    a = str(i)  # 숫자를 문자로 변경
    cnt = 0  # - 갯수를 세기 위해 cnt 설정.
    for j in a:  # 숫자 하나하나 보면서
        if j in ('3', '6', '9'):  # 3, 6, 9라면
            cnt += 1  # cnt 에 1 추가.
    if not cnt:  # 3, 6, 9 가 없다면
        print(a, end=' ')  # 그대로 출력
    else:  # 3, 6, 9가 있다면
        print('-'*cnt, end=' ')  # 그 갯수만큼 - 출력.
