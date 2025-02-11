# 문자열 비교

T = int(input())

for tc in range(1, T + 1):

    str1 = list(input())  # 짧
    str2 = list(input())  # 길


    def solve():

        len_str1 = len(str1)  # 짧은 문자열 길이
        len_str2 = len(str2)  # 긴 문자열 길이

        for i in range(len_str2 - len_str1 + 1):  # i: 비교하려는
            is_find = True  # 플래그 변수. 더 밖의 for 문에서 break 하기 위해.

            for j in range(len(str2)):  # 검사 인덱스
                if str1[j] != str2[i + j]:  # 다르면 검사 종료

                    is_find = False
                    break

            if is_find:  # 플래그 변수가 True 라면
                return 1
        return 0


    result = solve()
    print(f'#{tc} {result}')

    # def solve():
    #
    #     len_str1 = len(str1)  # 짧은 문자열 길이
    #     len_str2 = len(str2)  # 긴 문자열 길이
    #
    #     for i in range(len_str2 - len_str1 + 1):  # i: 비교하려는
    #
    #         for j in range(len(str2)):  # 검사 인덱스
    #             if str1[j] != str2[i + j]:  # 다르면 검사 종료
    #                 break
    #         else:
    #             return 1
    #
    #     return 0
