from collections import defaultdict
M = int(input())
N = int(input())
grid = []
for k in range(M):
    line = list(map(int, input().split()))
    grid.append(line)


def factors(num, M, N):
    l = 1
    facs = []
    while l <= num and l <= M + 1:
        i = 0
        while l * i <= num and i <= N + 1:
            if (l * i) == num:
                x = (l, i)
                facs.append(x)
            i += 1
        l += 1
    return facs


def pos_testing(pos):
  pos_lis = []
  for l in pos:
    if l[0] <= M and l[1] <= N:
      facs = factors(grid[l[0] - 1][l[1] - 1])
      for f in facs:
        if f not in pos:
          pos_lis.append(f)
  return pos_lis


pos = [(1, 1)]
last_pos = defaultdict(bool)
while (M, N) not in pos and last_pos[pos]:
  last_pos[pos] = True
  pos = pos_testing(pos)

if (M, N) in pos:
  print("yes")
else:
  print("no")
