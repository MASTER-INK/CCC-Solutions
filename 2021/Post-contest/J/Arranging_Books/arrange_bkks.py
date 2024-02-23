import time
r = int(input())
c = int(input())

grid = []
inputs = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(False)
    grid.append(row)

inputCount = int(input())

for i in range(inputCount):
    inputs.append(input())

for i in range(len(inputs)):
    direction = inputs[i].split(" ")[0]
    index = int(inputs[i].split(" ")[1]) - 1

    if direction == "R":
        for j in range(len(grid[index])):
            grid[index][j] = not grid[index][j]
    else:
        for j in range(len(grid)):
            grid[j][index] = not grid[j][index]

newArray = []
for i in range(len(grid)):
    newArray += grid[i]

print(newArray.count(True))
print(time.process_time())
