from collections import defaultdict


def factor_pairs(n):
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append([n // i, i])
            if i != n // i:
                factors.append([i, n // i])
    return factors


m = int(input())
n = int(input())

done = defaultdict(int)


# 0 == not in list
# 1 == in list and not done
#2 == done
# 3 == found but not done yet

grid = []
# could use dictionary with x and y values; may be faster

start = None

for y in range(m):
    line = list(map(int, input().split()))
    if start == None:
        start = line[0]
    for j in line:
        done[j] = 1
    grid.append(line)


"""m = 3
n = 4
grid = [[3, 10, 8, 14],
[1, 11, 12, 12],
[6, 2, 3, 9]]

start = 3

done = defaultdict(int)

for y in range(m):
    line = grid[y]
    if start == None:
        start = line[0]
    for j in line:
        done[j] = 1
    grid.append(line)"""



def end_find(start):
    c = 0
    max_c = 1
    todo = {0:start}
    while c < max_c:
        cur = todo[c]
        if done[cur] == 1 or done[cur] == 3:
            new_factors = factor_pairs(cur)
            for l in new_factors:
                if l[0] <= m and l[1] <= n:
                    num = grid[l[0] - 1][l[1] - 1]
                    if done[num] == 1:
                        todo[max_c] = num
                        done[num] = 3
                        max_c += 1
                if l[0] == m and l[1] == n:
                    return "yes"
        done[cur] = 2
        c += 1
    else:
        return "no"


print(end_find(start))
