a = '011110'
b = '111'

c = a.split(b)

while '' in c:
    c.remove('')

d = list(map(int, c))

print(d)