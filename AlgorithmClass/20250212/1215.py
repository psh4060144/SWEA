# 회문 1


def finding(field):  # 행렬의 행에서 회문을 찾는 함수
    count = 0  # 회문 갯수를 찾기 위해 변수를 설정.

    for row in range(8):  # 전체 행을 반복
        for col in range(8 - target + 1):  # 각 행의 열 하나씩을 시작점으로 설정. 회문 길이 이상을 범위로 하는 시작점을 선택하지 않기 위해.
            for char in range(target // 2):  # 회문 절반만 탐색
                if field[row][col + char] != field[row][col - char + target - 1]:  # 앞쪽과 뒷쪽을 모두 비교.
                    break  # 회문이 아니라면 다음 시작점으로.
            else:
                count += 1  # 회문이라면 갯수에 +1 해주고 다음 시작점으로.

    return count


T = 10  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    target = int(input())  # 회문 길이를 입력

    field = [list(input()) for _ in range(8)]  # 모든 데이터를 입력받아 하나의 행렬로 만듦.

    row_finding = finding(field)  # 행에서 회문을 탐색
    col_finding = finding(list(zip(*field)))  # 전치행렬을 통해 열에서 회문을 탐색

    print(f'#{tc} {row_finding + col_finding}')
