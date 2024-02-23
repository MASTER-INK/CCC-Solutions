import time
m = int(input("M "))
n = int(input("N "))
k = int(input("K "))
bg = [1, 0]
col = ["G", "B"]
grid = []

def paint(d, p, m, n):
    print(n)
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

print(time.process_time())


while k > 0:
    direction, place = input("input: ").split()
    place = int(place) - 1
    paint(direction, place, m, n)
    k -= 1

for line in range(m):
    for num in range(n):
        grid[line][num] = col[grid[line][num]]

print(grid)

gold_num = 0

for kj in grid:
    for l in kj:
        if l == "G":
            gold_num += 1

print(gold_num)
