a = [2, 1, 2, 1, 2]
n = len(a)
dec_a = 0

for i in range(n):
    dec_a += a[i] * (3**(n - i - 1))

print(dec_a)