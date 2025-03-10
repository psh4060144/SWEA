# 암호코드 스캔

hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010',
    '3': '0011', '4': '0100', '5': '0101',
    '6': '0110', '7': '0111', '8': '1000',
    '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110',
    'F': '1111',
}

code_dict = {
(3, 2, 1, 1) : 0,
(2, 2, 2, 1) : 1,
(2, 1, 2, 2) : 2,
(1, 4, 1, 1) : 3,
(1, 1, 3, 2) : 4,
(1, 2, 3, 1) : 5,
(1, 1, 1, 4) : 6,
(1, 3, 1, 2) : 7,
(1, 2, 1, 3) : 8,
(3, 1, 1, 2) : 9,
}


def solve():
    # 암호코드의 배율 찾기
    for i in range(N):
        j = M * 4 - 1
        while j > 0:
            if data[i][j] == '1':  # 암호코드 시작이라면
                c1, c2, c3, c4 = 0, 0, 0, 0
                while data[i][j] == '1':
                    c4 += 1
                    j -= 1
                while data[i][j] == '0':
                    c3 += 1
                    j -= 1
                while data[i][j] == '1':
                    c2 += 1
                    j -= 1
                while data[i][j] == '0':
                    c1 += 1
                    j -= 1
                ratio = (c1 + c2 + c3 + c4) // 7


            j -= 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    for r in range(N):
        new_row = ''
        for i in range(M):
            new_row += hex_to_bin[data[r][i]]
        data[r] = new_row
