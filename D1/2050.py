# 알파벳을 숫자로 전환

inputdata = list(input())
x = 0
b = []

def alphabetnum(alphabet):
    if ord(alphabet) < 97:
        return ord(alphabet) - 64
    else:
        return ord(alphabet) - 96

for _ in inputdata:
    a = inputdata[x]
    b.append(alphabetnum(a))
    x += 1

for i in b:
    print(i, end = " ")