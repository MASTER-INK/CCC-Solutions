n = 4
l = list(map(int, "3 1 3 4".split()))
sym = [0]

max_n = max(l)

for start in range(1, n):
    start_l = l[0:start + 1]
    x = 1
    cur_min = max_n
    for y in range(start + 2, n + 1):
        cur_sum = 0
        cur_l = l[x:y]
        x += 1

print(max_n, cur_min)
