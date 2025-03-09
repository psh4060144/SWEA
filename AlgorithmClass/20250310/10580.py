# 전봇대

T = int(input())  # test case
for tc in range(1, T + 1):  # test case 만큼 반복

    N = int(input())  # 전체 전선의 갯수를 입력
    line = [0] * 10001  # 전선 연결 상태를 표시하기 위해 빈 list 를 만듦.
    count = 0  # 전선 교차점을 세기 위해 변수를 설정.

    for i in range(N):  # 전선 갯수만큼 반복.
        a, b = map(int, input().split())  # 전선 연결 상태를 입력.

        for j in range(10001):  # 다른 전선의 연결 상태를 확인.
            if j < a:  # 왼쪽 전봇대의 전선 위치보다 아래의 전선이
                if line[j] > b:  # 오른쪽 전봇대의 전선 위치보다 위에 연결되어 있다면
                    count += 1  # 교차점이 발생.
            elif j > a:  # 마찬가지로 왼쪽 전봇대의 전선 위치보다 위의 전선이
                if line[j] < b and line[j]:  # 오른쪽 전봇대의 전선 위치보다 아래에 연결되어 있다면
                    count += 1  # 교차점이 발생.

        line[a] = b  # 교차점을 모두 센 후에 전선을 추가.

    print(f'#{tc} {count}')  # 양식에 맞게 출력.