T = 10  # test case의 갯수는 10으로 고정.

for i in range(T):  # 매 test case의 번호는 들어오므로 (1, T + 1)의 형태로 쓸 필요는 없음.

    N = int(input())  # 매 test case의 번호를 받음.

    ladder = [list(map(int, input().split())) for _ in range(100)]  # 100 * 100의 사다리를 받음

    for j in range(100):
        ladder[j].append(0)  # 마지막 열에 0을 추가.
        # 왜 0을 추가하는가? python은 -1 indexing이 가능하기 때문에 0번 index에서 올라갈 때
        # -1번을 indexing 하면 오른쪽 끝으로 간다. 따라서 그걸 막기 위해 마지막 열에 0을 추가.

    last_row = 99  # 바닥 행에서 출발하기 위해 바닥 인수를 설정
    arrive_idx = 0  # 현재 열을 찾는 인수 설정

    # idea
    # 사다리는 위에서 내려왔을 때와 아래에서 올라갔을 때의 결과가 같다.
    # 즉, 어디에서 출발해야 할 지 찾는다 == 도착 지점에서 끝까지 올라갔을 때의 자리를 찾는다.

    for col in ladder[last_row]:
        if col != 2:
            arrive_idx += 1  # 가장 아랫줄의 2를 찾고, 그 2의 열 번호로 시작한다.
        else:
            break

    while last_row != 0:  # 가장 윗줄에 도착할때까지 반복한다.

        # 자신 위치에서 살펴보아, 왼쪽과 오른쪽에 둘 다 1이 없을 때까지 올라간다.
        while ladder[last_row][arrive_idx - 1] != 1 and ladder[last_row][arrive_idx + 1] != 1:
            if last_row == 0:
                break
            last_row -= 1

        # 왼쪽에 1이 있는 경우, 1이 나오지 않을때까지 왼쪽으로 쭉 이동한다.
        if arrive_idx != 0 and ladder[last_row][arrive_idx - 1] == 1:
            while ladder[last_row][arrive_idx - 1] != 0:
                arrive_idx -= 1
            last_row -= 1

        # 오른쪽에 1이 있는 경우, 1이 나오지 않을때까지 오른쪽으로 쭉 이동한다.
        if arrive_idx != 99 and ladder[last_row][arrive_idx + 1] == 1:
            while ladder[last_row][arrive_idx + 1] != 0:
                arrive_idx += 1
            last_row -= 1

    print(f'#{N} {arrive_idx}')