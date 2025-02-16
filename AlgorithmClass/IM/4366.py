# 정식이의 은행 업무

T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    bit = list(map(int, input()))  # 2진수를 받음.
    bit_len = len(bit)  # 2진수의 길이를 구함.
    trit = list(map(int, input()))  # 3진수를 받음.
    trit_len = len(trit)  # 3진수의 길이를 구함.

    for i in range(len(bit)):  # 2진수의 모든 숫자를 하나씩 바꿔가며 비교.
        flag = False  # 가장 바깥의 for 문을 break 하기 위해 flag 변수 사용.
        bit_tmp = bit[i]  # 기존값 저장.
        if bit[i] == 1:  # 숫자를 하나 바꿈.
            bit[i] = 0
        else:
            bit[i] = 1

        dec_bit = 0
        for ii in range(bit_len):
            dec_bit += bit[ii] * (2 ** (bit_len - ii - 1))  # 바꾼 값을 10진수로 저장.

        for j in range(len(trit)):  # 3진수의 모든 숫자를 하나씩 바꿔가며 비교.
            trit_tmp = trit[j]  # 기존값 저장

            for k in range(3):  # 숫자를 하나 바꿈
                trit[j] = k

                dec_trit = 0
                for jj in range(trit_len):
                    dec_trit += trit[jj] * (3 ** (trit_len - jj - 1))  # 바꾼 값을 10진수로 저장.

                if dec_bit == dec_trit:  # 두 10진수의 값이 같다면
                    flag = True  # flag 변수를 True 로 바꾸고 break.
                    break

            trit[j] = trit_tmp  # 바꿨던 값 원복

            if flag:  # flag 변수로 판단.
                break

        bit[i] = bit_tmp  # 바꿨던 값 원복

        if flag:  # flag 변수로 판단
            break

    print(f'#{tc} {dec_bit}')