import time
m = int(input())
n = int(input())
k = int(input())
bg = [1, 0]
grid = []

def paint(d, p, m, n):
    if d == "R":
        for l in range(n):
            grid[p][l] = bg[grid[p][l]]
    else:
        for l in range(m):
            grid[l][p] = bg[grid[l][p]]


for i in range(m):
    line = []
    for l in range(n):
        line.append(1)
    grid.append(line)


while k > 0:
    direction, place = input().split()
    place = int(place) - 1
    paint(direction, place, m, n)
    k -= 1


gold_num = 0

for kj in grid:
    for l in kj:
        if l == 0:
            gold_num += 1

print(gold_num)
