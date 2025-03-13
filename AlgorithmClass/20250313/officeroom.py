# 회의실 배정

# 활동 선택 (Activity-selection problem)
# 시작 시간과 종료 시간이 주어질 때, 가장 많은 활동을 선택하는 경우 최대 몇 개를 선택할 수 있는가?

# 1. 활동 종료 시간을 기준으로 오름차순 정렬
# 2. 종료 시간이 가장 빠른 회의를 확정
# 3. 확정한 회의의 종료 시간 이후에 있는 시작 시간이 가장 빠른 회의를 확정.
# 4. 3번을 반복하여 뽑음.

"""
5 9 6 10 8 11 1 4 3 5 1 6 5 7 3 8 2 13 12 14
"""

data = list(map(int, input().split()))
activities = []
N = len(data)
for i in range(0, N, 2):
    # data[i] = 시작, data[i + 1] = 종료
    activities.append((data[i], data[i + 1]))
print(activities)

# 종료 시간 기준으로 오름차순 정렬
activities.sort(key=lambda x: x[1])
print(activities)

selected_activities = []
prev_end = 0

for activity in activities:
    # 시작 시간이 이전 종료 시간 이후라면 선택.
    if activity[0] >= prev_end:
        selected_activities.append(activity)
        prev_end = activity[1]

print(selected_activities)