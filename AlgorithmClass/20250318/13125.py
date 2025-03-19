# 전기 버스 2


def battery(idx, cnt):  # 최소 교환 횟수를 찾는 함수.
    global cnt_min  # 최소 교환 횟수를 찾기 위해 전역 변수를 설정.

    if cnt_min <= cnt:  # 현재 교환 횟수가 이미 최소 교환 횟수보다 크거나 같다면 가망이 없으므로 종료.
        return  # pruning.

    if idx >= N:  # 종점에 도착했다면
        if cnt_min > cnt:  # 최소 교환 횟수와 현재 교환 횟수를 비교하여
            cnt_min = cnt  # 더 작은 값을 최소 교환 횟수로.
            return  # 이후 종료.
        return  # 현재 교환 횟수가 최소 교환 횟수보다 같거나 크다면 그냥 종료.

    watt = M[idx]  # 배터리 용량을 변수로 설정.
    for i in range(watt, 0, -1):  # 최대한 멀리 갈 수 있는 곳부터 거꾸로 탐색.
        battery(idx + i, cnt + 1)  # 다음 정류장으로 이동하며, 교환 횟수 1 추가.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.
    N, *M = map(int, input().split())  # 정류장 수 N, 정류장 별 배터리 M 을 받음.
    M = [0] + M  # indexing 을 편하게 하기 위해 앞에 0을 추가.
    cnt_min = N  # 최소 교환 횟수를 찾기 위해 변수를 설정.
    battery(1, 0)  # 최소 교환 횟수를 찾는 함수 실행.
    print(f'#{tc} {cnt_min - 1}')  # 양식에 맞게 출력.
