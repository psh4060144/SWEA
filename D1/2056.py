# 연월일 달력

linetotal = int(input())
inputdata = list(input() for _ in range(linetotal))
x = 0

def minusone():
    print(f'#{x+1} {-1}')

def ymd(a):
    print(f'#{x+1} {a[0:4]}/{a[4:6]}/{a[6:8]}')

def calender(a):
    if a[4:6] in ('01', '03', '05', '07', '08', '10', '12'):
        if int(a[6:8]) > 31:
            minusone()
        else:
            ymd(a)
    elif a[4:6] in ('04', '06', '09', '11'):
        if int(a[6:8]) > 30:
            minusone()
        else:
            ymd(a)
    elif a[4:6] == '02':
        if int(a[6:8]) > 28:
            minusone()
        else:
            ymd(a)
    else:
        minusone()

for _ in inputdata:
    a = inputdata[x]
    calender(a)
    x += 1