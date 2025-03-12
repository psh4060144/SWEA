# 전자카트

def solve(x, lst, count):  # 최소 배터리 사용량을 구하는 함수.
    global battery  # 최소 배터리 사용량을 찾기 위해 변수를 설정.
    global cnt  # 현재 배터리 사용량을 찾기 위해 변수를 설정.

    if count == N:  # 관리구역 끝까지 돌았을 경우
        if battery > cnt + field[x][0]:  # 최소 배터리 사용량이 처음으로 돌아올 때까지의 배터리 사용량보다 크다면
            battery = cnt + field[x][0]  # 현재 배터리 사용량을 최소 배터리 사용량으로.
            return  # 전역 변수를 수정했기 때문에 따로 return 값을 주지 않아도 됨.

    for i in range(N):  # 관리구역 갯수만큼 반복.
        if i not in lst:  # 가지 않았던 관리구역일 경우
            cnt += field[x][i]  # 해당 관리구역의 배터리 사용량을 추가.
            lst.append(i)  # 해당 관리구역을 방문 list 에 추가.
            solve(i, lst, count + 1)  # 해당 관리구역, 방문 list, 방문한 관리구역 갯수로 재귀 실행.
            lst.pop()  # 재귀가 끝난 후 해당 관리구역에서 빠져나옴.
            cnt -= field[x][i]  # 배터리 사용량도 사용하지 않은 때로 돌려줌.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N = int(input())  # 관리구역 갯수를 입력.
    field = [list(map(int, input().split())) for _ in range(N)]  # 관리구역 별 배터리 사용량을 입력.
    battery = 1001  # 최대 배터리 사용량을 입력. 최소 배터리 사용량은 무조건 이것보다 적음.
    cnt = 0  # 현재 배터리 사용량을 0으로 설정.

    solve(0, [0], 1)  # 최소 배터리 사용량을 구하는 함수 실행.

    print(f'#{tc} {battery}')  # 양식에 맞게 출력.
