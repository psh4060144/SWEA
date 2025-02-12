# 어디에 단어가 들어갈 수 있을까

# idea
# 단어 길이와 정확히 같은 수의 칸만을 가지는 공간에 넣을 수 있다.
# 테두리에 0을 추가해주고, 단어 길이 양 끝에 0을 추가해서 011110 처럼 만들어 주면,
# 정확히 같은 수의 칸만을 찾을 수 있다.

def add_zeros(list):  # 왼쪽, 오른쪽 열 혹은 단어에 0을 추가하는 함수.
    list.insert(0, 0)
    list.append(0)

def judge(field, target):  # 들어갈 수 있는 횟수를 세는 함수.
    count = 0
    
    for row in range(1, N + 1):
        for col in range(N - K + 1):                  # 해당 행을 왼쪽부터 가능한 만큼 반복하면서
            for i in range(K + 2):                    # 넣고 싶은 단어의 글자 수를 비교하여
                if target[i] != field[row][col + i]:  # 들어갈 수 없다면 break.
                    break
            else:
                count += 1                            # 들어갈 수 있다면 count에 1을 추가.
    
    return count

T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    N, K = list(map(int, input().split()))  # 퍼즐의 길이, 원하는 단어의 길이를 받음

    target = [1] * K   # 단어는 길이만큼 1을 추가하여
    add_zeros(target)  # 양 끝에 0을 추가.
    field = []  # 빈 field를 생성.

    for _ in range(N):
        line = list(map(int, input().split()))  # line을 하나씩 받아
        add_zeros(line)                         # 양 끝에 0을 추가하고
        field.append(line)                      # field에 붙인다.

    field.insert(0, [0] * (N + 2))  # field 위 아래에
    field.append([0] * (N + 2))     # 0으로만 이루어진 line을 붙인다.

    row_judge = judge(field, target)  # 행을 살펴보며 들어갈 수 있는 횟수를 count.
    col_judge = judge(list(zip(*field)), target)  # 전치행렬을 통해 열을 살펴보며 들어갈 수 있는 횟수를 count.

    print(f'#{tc} {row_judge + col_judge}')