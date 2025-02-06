# 숫자 카드

T = int(input())  # test case의 총 갯수를 인수로 저장.

for i in range(1, T + 1):  # test case만큼 반복.

    N = int(input())  # 카드의 장수를 인수로 저장.
    aj = list(map(int, input()))  # 카드의 숫자를 하나씩 뜯어 list 형태로 변환
    counts = [0] * 10  # 0 ~ 9 까지의 수가 있으므로 칸을 10개 만들어 줌.

    for j in range(N):  # 카드의 장수만큼 반복
        counts[aj[j]] += 1  # 카드의 갯수를 카운팅. 같은 숫자가 나올때마다 count의 해당 index가 증가.
    
    max_num = 0  # 카드의 최댓값을 인수로 설정하기 위해 기본 인수를 설정.
    max_idx = 0  # 카드의 위치를 인수로 설정하기 위해 기본 인수를 설정.

    for k in range(len(counts)):  # counts의 길이만큼 반복한다. 근데 나는 counts의 길이를 10으로 고정했으므로 len(counts) 대신 10을 넣어도 됐었다.
        if max_idx <= counts[k]:  # 카드의 갯수가 제일 많은 카드의
            max_idx = counts[k]   # 위치를 넣고
            max_num = k           # 카드의 숫자도 넣는다.
    
    print(f'#{i} {max_num} {max_idx}')  # 출력.