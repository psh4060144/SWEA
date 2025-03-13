# 컨테이너 운반

T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N, M = map(int, input().split())  # N 개의 컨테이너, M 개의 트럭.
    N_container = list(map(int, input().split()))  # 컨테이너 각각의 무게.
    M_truck = list(map(int, input().split()))  # 트럭 각각의 적재 용량.

    N_container.sort(reverse=True)
    M_truck.sort(reverse=True)  # 컨테이너와 트럭을 각각 역순으로 정렬.

    weight = 0  # 옮겨진 화물의 전체 무게를 출력하기 위해 변수를 설정.
    for i in range(M):  # 적재 용량이 큰 트럭부터 순회하면서
        for j in range(N):  # 무게가 많이 나가는 컨테이너를 살펴봄.
            if M_truck[i] >= N_container[j]:  # 트럭의 적재 용량이 컨테이너보다 크다면
                weight += N_container[j]  # 그 컨테이너를 싣고 나감. 화물 무게에 추가.
                N_container[j] = 51  # 컨테이너 자리에는 큰 수를 입력해서 더 싣지 못하게 함.
                break  # 이후 다음 트럭을 확인.

    print(f'#{tc} {weight}')  # 양식에 맞게 출력.
