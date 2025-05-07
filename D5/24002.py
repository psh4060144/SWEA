# 쪼개기

# idea
# 기본적으로 짝수 길이의 막대는 한 종류의 막대가 생기지만, 홀수 길이의 막대는 두 종류의 막대가 생긴다.
# 또한 홀수 길이의 막대는 인접한 짝수 길이의 막대의 자식 막대를 항상 포함한다. (15 -> 7, 8 / 14 -> 7 / 16 -> 8)
# 따라서, 막대를 확정할 때 홀수 길이의 막대를 확정하는 것이 웬만하면 옳다.
# but 그러면 여러 반례가 생기는데, 특히 가장 짧은 막대가 좀 많이 짧을 때, 즉 1, 2, 3 일 때 생긴다.
# 또, 가장 긴 막대와 가장 짧은 막대의 길이 차이가 얼마 나지 않을 때, 즉 1, 2 일 때 생긴다.
# 예외 처리만 잘 해주면 풀리는 문제.

T = int(input())
for tc in range(1, T + 1):

    N = int(input())  # 막대 갯수.
    stick = list(map(int, input().split()))  # 막대 정보.
    cnt = 0  # 막대를 쪼개는 횟수.

    while True:  # 일단 무한대로 돈다.
        min_v = 10000000001
        min_idx = -1
        max_v = -1
        max_idx = -1

        for i in range(N):
            if stick[i] < min_v:
                min_v, min_idx = stick[i], i
            if stick[i] > max_v:
                max_v, max_idx = stick[i], i  # 최솟값, 최솟값의 index, 최댓값, 최댓값의 index 를 확인.

        if max_v == min_v:
            break  # 최솟값과 최댓값이 같다면 더 쪼갤 필요가 없다.

        if min_v % 2:  # 최솟값이 홀수라면
            if stick[max_idx] - stick[min_idx] == 2:  # 최댓값과의 차이가 2일 때
                if stick[min_idx] in (1, 3):  # 최솟값이 1 또는 3이라면
                    cnt += N - stick.count(stick[min_idx])  # 최솟값을 제외한 막대 갯수만큼 cnt 추가.
                else:  # 최솟값이 5 이상이라면
                    cnt += N  # 전체 갯수만큼 cnt 추가.
                break  # 이후 더 쪼갤 필요가 없으므로 while 문을 빠져나간다.

            elif stick[max_idx] - stick[min_idx]:  # 최댓값과의 차이가 2가 아니라면
                a, b = stick[max_idx] // 2, stick[max_idx] - (stick[max_idx] // 2)  # 최댓값 막대를 쪼개
                if a == stick[min_idx] or b == stick[min_idx]:  # 최솟값과 같은 막대가 있다면
                    stick[max_idx] = stick[min_idx]  # 그 막대를 선택.
                    cnt += 1  # cnt 추가.
                else:  # 최솟값과 같은 막대가 없다면
                    if a % 2:
                        stick[max_idx] = a
                    else:
                        stick[max_idx] = b  # 둘 중 홀수 길이인 막대를 선택.
                    cnt += 1  # cnt 추가.

        else:  # 최솟값이 짝수라면
            if stick[max_idx] - stick[min_idx] == 1:  # 최댓값과의 차이가 1일 때
                if stick[max_idx] == 3:  # 최댓값이 3이라면
                    cnt += stick.count(3)  # 3의 갯수만큼 cnt 추가.
                else:  # 최댓값이 3이 아니라면
                    cnt += N  # 전체 갯수만큼 추가.
                break  # 이후 더 쪼갤 필요가 없다.

            else:  # 최댓값과의 차이가 1이 아니라면
                a, b = stick[max_idx] // 2, stick[max_idx] - (stick[max_idx] // 2)  # 최댓값 막대를 쪼개
                if a == stick[min_idx] or b == stick[min_idx]:  # 최솟값과 같은 막대가 있다면
                    stick[max_idx] = stick[min_idx]  # 그 막대를 선택.
                    cnt += 1  # cnt 1 추가.
                else:  # 최솟값과 같은 막대가 없다면
                    if a % 2:
                        stick[max_idx] = a
                    else:
                        stick[max_idx] = b  # 둘 중 홀수 길이인 막대를 선택.
                    cnt += 1  # cnt 추가.

    print(cnt)  # cnt 출력.
