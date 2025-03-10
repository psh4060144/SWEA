T = int(input())
for tc in range(1, T + 1):

    day_total = int(input())
    lst = list(map(int, input().split()))
    lstsum = 0
    dic = {a:b for b,a in enumerate(lst)}


    while lst != []:
        lst_max = lst.index(max(lst))

        lst1 = lst[:lst_max + 1]
        lst2 = lst[lst_max + 1:]

        lst1_max = lst1.pop()
        lstsum += lst1_max * len(lst1) - sum(lst1)
        lst = lst2

    print(f'#{tc} {lstsum}')
