# 단순 2진 암호코드

dictionary = {  # 암호 코드를 불러옴.
    (0, 0, 0, 1, 1, 0, 1): 0,
    (0, 0, 1, 1, 0, 0, 1): 1,
    (0, 0, 1, 0, 0, 1, 1): 2,
    (0, 1, 1, 1, 1, 0, 1): 3,
    (0, 1, 0, 0, 0, 1, 1): 4,
    (0, 1, 1, 0, 0, 0, 1): 5,
    (0, 1, 0, 1, 1, 1, 1): 6,
    (0, 1, 1, 1, 0, 1, 1): 7,
    (0, 1, 1, 0, 1, 1, 1): 8,
    (0, 0, 0, 1, 0, 1, 1): 9,
}

T = int(input())  # test case
for tc in range(1, T + 1):  # test case 만큼 반복

    N, M = map(int, input().split())  # 세로 크기 N, 가로 크기 M 을 입력

    for i in range(N):
        tmp = list(map(int, input()))  # 모든 입력을 받아오는데
        if 1 in tmp:  # 1이 있는 값이라면(암호가 섞여있는 줄이라면)
            barcode = tmp  # 그 입력을 저장

    num_list = []  # 암호를 정수화하여 추출하기 위해 빈 list 를 만듦.
    for j in range(M - 1, -1, -1):  # 오른쪽 끝에서 읽어오는데
        if barcode[j] == 1:  # 1을 만난다면(암호의 끝에 도달한다면)
            for k in range(j - 55, j + 1, 7):  # 암호의 처음부터 7개씩 끊어서 정수화 함.
                tmp_list = (barcode[k],
                            barcode[k + 1],
                            barcode[k + 2],
                            barcode[k + 3],
                            barcode[k + 4],
                            barcode[k + 5],
                            barcode[k + 6])
                result = dictionary[tmp_list]  # 암호 코드에서 일치하는 key 의 value 값을 불러와
                num_list.append(result)  # list 에 추가.
            break  # 모든 값을 추가했다면 즉시 종료.

    def_sum = 0  # 함수가 유효한지 판단하기 위해 변수를 설정.
    for l in range(8):
        if (l+1) % 2:
            def_sum += num_list[l] * 3
        else:
            def_sum += num_list[l]  # 조건에 맞게 변수를 설정.

    if def_sum % 10 == 0:  # 유효하다면
        print(f'#{tc} {sum(num_list)}')  # 암호의 숫자를 모두 더해 출력
    else:
        print(f'#{tc} 0')  # 유효하지 않다면 0 출력