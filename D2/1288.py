# 새로운 불면증 치료법

line_total = int(input())

for i in range(1, line_total + 1):
    N = input()
    N_int = int(N)
    N_numcount = list(map(int,(list(N))))
    total_len = 0
    repeat = 1
    while total_len < 10:
        repeat += 1
        times_int = repeat * N_int
        times_int_lst = list(map(int,list(str(times_int))))
        N_numcount.extend(times_int_lst)
        total_len = len(set(N_numcount))
    print(f'#{i} {int(N) * repeat}')