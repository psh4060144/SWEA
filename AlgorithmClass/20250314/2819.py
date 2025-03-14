# 격자판의 숫자 이어 붙이기

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌 delta.


def dfs(sr, sc, count):  # 모든 격자판을 돌아보는 함수
    global mainlst  # 모든 경우의 수를 찾기 위해 전역 변수를 설정.
    stack = [(sr, sc, count)]  # 깊이 우선 탐색을 하기 위해 stack 을 만들고, 현재 위치를 추가.
    lst = [0] * 7  # 각 격자판의 숫자를 입력하기 위해 list 를 제작.

    while stack:  # stack 이 빌 때까지 반복.
        cr, cc, cnt = stack.pop()  # 현재 위치를 stack 의 끝에서 추출.
        value = field[cr][cc]  # 현재 격자판의 숫자를 구해서
        lst[cnt] = value  # 격자판 list 의 해당 위치에 기입.
        if cnt == 6:  # 격자판 입력을 완료했다면
            copylst = tuple(lst)  # set 에 넣어주기 위해 lst 를 tuple 로 바꿔줌.
            mainlst.add(copylst)  # 이후 set 에 추가.
            continue  # 이후 다음 반복으로 이동. 마지막 위치의 격자판을 다시 뽑게 됨.
        for i in range(4):  # 상하좌우 4칸을 보면서
            nr = cr + delta[i][0]
            nc = cc + delta[i][1]  # 이동할 위치를 저장.
            if 0 <= nr < 4 and 0 <= nc < 4:  # 유효한 위치라면
                stack.append((nr, nc, cnt + 1))  # stack 에 추가.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    field = [list(map(int, input().split())) for _ in range(4)]  # 갹자판을 입력.
    mainlst = set()  # 모든 경우의 수를 받기 위해 빈 set 를 만듦. 중복을 허용하지 않기 위해.

    for row in range(4):
        for col in range(4):
            dfs(row, col, 0)  # 격자판의 각 판에서 모든 격자판을 돌아보는 함수를 실행.

    print(f'#{tc} {len(mainlst)}') # 양식에 맞게 출력.
