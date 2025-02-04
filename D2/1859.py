import sys

case_total = int(sys.stdin.readline())

for repeat in range(case_total):

    day_total = int(sys.stdin.readline())
    lst = list(map(int,sys.stdin.readline().split()))

    lstsum = 0
    dic = {a:b for b,a in enumerate(lst)}


    while lst != []:
        lst_max = lst.index(max(lst))

        lst1 = lst[:lst_max + 1]
        lst2 = lst[lst_max + 1:]

        lst1_max = lst1.pop()
        lstsum += lst1_max * len(lst1) - sum(lst1)
        lst = lst2

    print(f'#{repeat + 1} {lstsum}')


