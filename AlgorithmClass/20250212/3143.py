# 가장 빠른 문자열 타이핑

T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    A, B = input().split()  # 글자를 나눠서 받음
    A = list(A)
    B = list(B)  # 각각 list 화.

    start = 0  # 같은 글자를 찾는 곳을 정하기 위해 변수를 설정
    count = 0  # 타이핑 횟수를 세기 위해 변수를 설정

    while start <= len(A) - len(B) + 1:  # 마지막에 B 길이만큼 찾고 나면 종료

        for i in range(len(B)):  # B 길이만큼 반복
            if A[i + start] != B[i]:  # 같은 부분이 아닐 경우
                start += 1  # 바로 옆 칸으로 넘어가고
                count += 1  # 방금 기준 삼았던 글자는 타이핑
                break
        else:  # 같은 부분이라면
            start = start + i + 1  # 통째로 넘어가 그 다음 칸을 기준으로 잡고
            count += 1  # 전체를 한 번 타이핑

    count += len(A) - start  # 남은 길이만큼 타이핑
    print(f'#{tc} {count}')