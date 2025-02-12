# 회문 2

import sys
sys.stdin = open('palindrome_input.txt', 'r')


def finding(field):  # 모든 행의 회문을 찾아보는 함수를 제작
    len_max = 0  # 최대 길이를 찾기 위해 변수를 설정
    for row in range(100):  # 모든 행에 대해 수행
        start = 0  # 시작 지점을 설정

        for col in range(100 - start + 1):  # 모든 시작 지점으로부터 수행
            length = 0  # 열마다 회문 찾기 이전에 length 변수로 찾을 회문의 길이를 설정

            while length <= 100 - col:  # 시작지점부터 길이가 최대인 회문을 검색할 때까지 수행
                for char in range(length // 2):  # 회문 길이 절반만큼 탐색
                    if field[row][col + char] != field[row][col - char + length - 1]:  # 앞 절반과 뒷 절반이 다르면
                        break  # 탐색 종료
                else:  # 같으면 회문이므로
                    if len_max < length:
                        len_max = length  # 길이를 len_max에 반영

                length += 1  # 회문 길이를 1 늘림
        start += 1  # 시작 지점을 한 칸 옆으로 옮김
    return len_max


T = 10  # test case

for i in range(T):  # 모든 test case 에 대해 수행

    tc = input()  # test case 의 번호를 받음

    field = [list(input()) for _ in range(100)]  # 모든 행렬을 field 로 받음

    row_finding = finding(field)  # 모든 행에 대해 최대 회문 길이를 찾음
    col_finding = finding(list(zip(*field)))  # 전치행렬을 이용해 모든 열에 대해 최대 회문 길이를 찾음

    print(f'#{tc}', end=' ')
    if row_finding >= col_finding:  # 둘 중 더 큰 값을 출력.
        print(row_finding)
    else:
        print(col_finding)
