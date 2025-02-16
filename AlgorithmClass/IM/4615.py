# 재미있는 오셀로 게임

T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    N, M = map(int, input().split())  # 보드 한 변의 길이, 돌을 놓는 횟수

    field = [[0] * N for _ in range(N)]  # 보드 판을 0으로 꽉 채움
    field[N // 2 - 1][N // 2 - 1] = 2
    field[N // 2][N // 2] = 2
    field[N // 2 - 1][N // 2] = 1
    field[N // 2][N // 2 - 1] = 1  # 보드 중간에 기본 돌을 놓음

    delta_row = [-1, -1, 0, 1, 1, 1, 0, -1]
    delta_col = [0, 1, 1, 1, 0, -1, -1, -1]  # 12시부터 시계방향 delta.

    for _ in range(M):  # 돌을 놓는 횟수만큼 반복
        row, col, color = map(int, input().split())  # 돌의 위치와 색깔을 받음.
        row -= 1
        col -= 1  # 보드는 0칸이 아닌 1칸부터 시작이므로 들어오는 정보에서 1을 빼야 0부터 시작하게 할 수 있음.
        field[row][col] = color  # 해당 위치에 돌을 놓음
        
        for i in range(8):  # 8방향을 보는데,
            
            if 0 <= row + delta_row[i] < N and 0 <= col + delta_col[i] < N and field[row][col] != field[row + delta_row[i]][col + delta_col[i]] and field[row + delta_row[i]][col + delta_col[i]] != 0:
                # 선택한 방향이 판을 벗어나지 않고, 선택한 방향에 돌이 있으며, 그 돌의 색깔이 놓은 돌과 다르다면
                
                for j in range(1, N):  # 그 방향으로 한 칸씩 넘어가며 본다.
                    
                    if 0 <= row + delta_row[i] * j < N and 0 <= col + delta_col[i] * j < N:  # 판 위의 칸만 볼 때,
                        
                        if field[row + delta_row[i] * j][col + delta_col[i] * j] == 0:  # 같은 색의 돌을 만나기 전 0을 만난다면
                            
                            break  # 즉시 종료
                        
                        elif field[row][col] == field[row + delta_row[i] * j][col + delta_col[i] * j]:  # 놓은 돌과 같은 색의 돌을 만난다면,
                            
                            for k in range(1, j + 1):  # 그 이전의 모든 돌을 뒤집어서
                                
                                field[row + delta_row[i] * k][col + delta_col[i] * k] = field[row][col]  # 놓은 돌의 색과 같게 한다.
                            
                            break  # 이후 종료
    
    black = 0
    white = 0  # 돌의 갯수를 세기 위해 변수를 설정.
    
    for l in range(N):
        for m in range(N):
            if field[l][m] == 1:
                black += 1
            elif field[l][m] == 2:  # field 위의 모든 돌을 보고 갯수를 셈.
                white += 1

    print(f'#{tc} {black} {white}')