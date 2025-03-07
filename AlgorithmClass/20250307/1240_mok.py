code_dict = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9,
}


# 암호 코드를 스캔해서 결과를 반환하는 함수
def solve():
    # 암호코드를 읽어오기, 암호코드 7*8 = 56개
    # 배경 0, 암호코드의 시작 0 하나일 수도 있고 2개 일수도 있고....3
    for i in range(N):
        # 행을 탐색할 때 뒤에서 부터 탐색, 코드 길이가 56이니까.. 55번까지 확인
        for j in range(M - 1, 54, -1):  # # for j in range(-1, -M, -1):
            if data[i][j] == 1:  # 암호 코드의 끝을 찾음!
                # 암호코드 읽어오기
                # 숫자 하나 읽기 * 8
                code = []  # 숫자 8개로 이루어진 코드를 저장할 리스트
                for _ in range(8):
                    # 숫자 하나 읽기
                    # 1읽고
                    # 0읽고
                    # 1읽고
                    # 0읽고
                    # 0과 1의 개수를 저장하기 위한 변수
                    c1, c2, c3, c4 = 0, 0, 0, 0
                    # 1의 개수 세기
                    while data[i][j] == 1:
                        c4 += 1
                        j -= 1
                    while data[i][j] == 0:
                        c3 += 1
                        j -= 1
                    while data[i][j] == 1:
                        c2 += 1
                        j -= 1
                    # while data[i][j] == 0:
                    #     c1 += 1
                    #     j -= 1
                    c1 = 7 - c2 - c3 - c4
                    j -= c1
                    # print(code_dict[(c1, c2, c3, c4)])
                    code.append(code_dict[(c1, c2, c3, c4)])
                # print(code)
                # 코드 유효성 검사
                odd_sum = code[1] + code[3] + code[5] + code[7]
                even_sum = code[0] + code[2] + code[4] + code[6]
                if (odd_sum * 3 + even_sum) % 10 == 0:
                    return odd_sum + even_sum
                else:
                    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input())) for _ in range(N)]
    result = solve()
    print(f'#{tc} {result}')
    # for row in data:
    #     print(row)