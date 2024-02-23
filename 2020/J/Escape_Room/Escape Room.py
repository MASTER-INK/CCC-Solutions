M = int(input())
N = int(input())
grid = []
for k in range(M):
    line = input().split()
    grid.append(line)


def factors(num, M, N):
    l = 1
    facs = []
    while l < num and l <= M + 1:
        i = 0
        while l * i <= num and i <= N + 1:
            if (l * i) == num:
                x = (l, i)
                facs.append(x)
            i += 1
        l += 1
    return facs


pos_num = 0
oldest_pos = []
old_pos = []
pos = (1, 1)
while pos != (M, N) and old_pos not in oldest_pos:
    oldest_pos.append(old_pos)
    pos = (1, 1)
    facs = factors(int(grid[pos[0] - 1][pos[1] - 1]), M, N)
    old_pos = []
    while pos != (M, N) and len(facs) > 0 and pos not in old_pos and pos_num < len(facs):
        old_pos.append(pos)
        pos = facs[pos_num]
        facs = factors(int(grid[pos[0] - 1][pos[1] - 1]), M, N)
    pos_num += 1


if pos == (M, N):
    print("yes")
else:
    print("no")
