# 두 개의 숫자열

total = int(input())
linetotal = 3 * total
input_data = list(input() for _ in range(linetotal))
x = 0
d = []

def max_sum(ai, bj):
    k = 0
    l = 0
    c = []
    if len(ai) > len(bj):
        ai, bj = bj, ai
    
    if len(ai) < len(bj):
        while l < len(bj) - len(ai) + 1:
            k = 0
            for i in ai:
                c.append(ai[k]*bj[k+l])
                k += 1
            d.append(sum(c))
            c.clear()
            l += 1
        d.sort()
        print("#%d" % (x/3), d.pop())
    else:
        while l < len(ai):
            c.append(ai[l]*bj[l])
            l += 1
        d.append(sum(c))
        c.clear()
        d.sort()
        print("#%d" % (x/3), d.pop())

while x < linetotal:
    a = input_data[x]
    a = list(map(int, a.split()))
    ai = input_data[x + 1]
    ai = list(map(int, ai.split()))
    bj = input_data[x + 2]
    bj = list(map(int, bj.split()))
    x += 3
    max_sum(ai, bj)
    d.clear()