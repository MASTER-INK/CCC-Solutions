import time
m = int(input())
n = int(input())
k = int(input())
bg = [1, 0]
col = ["G", "B"]
grid = []

def paint(d, p, m, n):
    if d == "R":
        grid[p][0] = bg[grid[p][0]]
    else:
        for l in range(n):
            grid[l][p] = bg[grid[l][p]]


for i in range(m):
    grid.append("1" * n)

print(time.process_time())

while k > 0:
    direction, place = input().split()
    place = int(place) - 1
    paint(direction, place, m, n)
    k -= 1
    for kj in grid:
        print(kj)

for line in range(m):
    for num in range(n):
        grid[line][num] = col[grid[line][num]]

for kj in grid:
    colstr = ""
    for l in kj:
        colstr += l
    print(colstr)
