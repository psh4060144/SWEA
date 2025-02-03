case_total = int(input())

for repeat in range(case_total):

    day_total = int(input())
    lst = list(map(int,input().split()))

    lstsum = 0

    while lst != []:
        lst_max = lst.index(max(lst))
        lst1 = lst[:lst_max + 1]
        lst2 = lst[lst_max + 1:]

        lst1_max = lst1.pop()
        lstsum += lst1_max * len(lst1) - sum(lst1)
        lst = lst2

    print(f'#{repeat + 1} {lstsum}')