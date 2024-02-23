import time

with open("Modern_inputs.txt") as input_numbs:
    file_inp = []
    for i in input_numbs:
        file_inp.append(i.strip())

m = int(file_inp[0])
n = int(file_inp[1])
k = int(file_inp[2])
bg = [1, 0]
col = ["G", "B"]
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

print(time.process_time())


while k > 0:
    direction, place = file_inp[(len(file_inp) - k)].split()
    place = int(place) - 1
    paint(direction, place, m, n)
    k -= 1



gold_num = 0

for kj in grid:
    for l in kj:
        if l == 0:
            gold_num += 1
gold_place = []
for i in range(m):
    for l in range(n):
        if grid[i][l] == 0:
            pos = (i, l)
            gold_place.append(pos)
print(sorted(gold_place))

print(gold_num)
print(time.process_time())
