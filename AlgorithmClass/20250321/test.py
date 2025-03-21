N = 6
subset = [(0, 1, 2), (0, 4, 5)]


tmp_A = subset[0]
tmp_B = tuple(set(range(N)) - set(subset[0]))

print(tmp_A, tmp_B)

tmp_A = subset[1]
tmp_B = tuple(set(range(N)) - set(subset[1]))

print(tmp_A, tmp_B)