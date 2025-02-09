# 스도쿠 검증

T = int(input())  # 전체 test case 입력

for i in range(1, T + 1):

    judge = 1  # 유효한지 판단하기 위해 변수를 설정.
    sudoku = [list(map(int, input().split())) for _ in range(9)]  # 들어오는 9개의 list를 받아 스도쿠로 제작

    for row in range(9):        
        ex_lst_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 행이 바뀔때마다 테스트용 list를 초기화.
        
        for col in range(9):
            if sudoku[row][col] in ex_lst_row:  # 해당 행을 참고하여 ex_lst_row에서 중복값을 제거
                ex_lst_row.remove(sudoku[row][col])
            
        if len(ex_lst_row) != 0:  # ex_lst_row의 길이가 0이다: 겹치는 값이 없다. / 길이가 0이 아니다: 겹친다.
            judge -= 1  # 겹치면 유효 판단 변수에서 1을 뺀다.

    for row in range(9):
        ex_lst_col = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 열이 바뀔때마다 테스트용 list를 초기화.
        
        for col in range(9):
            if sudoku[col][row] in ex_lst_col:  # 해당 행을 참고하여 ex_lst_col에서 중복값을 제거.
                ex_lst_col.remove(sudoku[col][row])
            
        if len(ex_lst_col) != 0:  # 위의 유효 판단과 동일.
            judge -= 1

    row_dir = [-1, -1, 0, 1, 1, 1, 0, -1, 0]  # 각 3x3 박스의 중간을 기준으로,
    col_dir = [0, 1, 1, 1, 0, -1, -1, -1, 0]  # 12시의 요소부터 시계방향으로 8방향, 마지막 본인까지 추가.

    for row in range(3):
        for col in range(3):
            ex_lst_sqr = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 매 3x3 박스마다 테스트용 list를 초기화.
            
            for j in range(9):
                if sudoku[3 * row + 1 + row_dir[j]][3 * col + 1 + col_dir[j]] in ex_lst_sqr:  # 해당 박스를 참고하여 ex_lst_sqr에서 중복값을 제거.
                    ex_lst_sqr.remove(sudoku[3 * row + 1 + row_dir[j]][3 * col + 1 + col_dir[j]])
                    
            if len(ex_lst_sqr) != 0:  # 위의 유효 판단과 동일.
                judge -= 1

    if judge == 1:
        print(f'#{i} {1}')
    else:
        print(f'#{i} {0}')  # 유효 판단 변수 == 1: 문제가 없다. / 유효 판단 변수 != 1: 문제가 있다.