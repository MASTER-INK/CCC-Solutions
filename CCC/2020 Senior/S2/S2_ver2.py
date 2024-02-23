from collections import defaultdict

"""m = 3
n = 4
grid = [[3, 10, 8, 14],
        [1, 11, 11, 11],
        [6, 2, 3, 9]]

positions = defaultdict(list)

done = defaultdict(bool)

for y in range(m):
    line = grid[y]
    for x in range(n):
        positions[line[x]].append(x * y)"""
        
m = int(input())
n = int(input())

grid = []

positions = defaultdict(list)

done = defaultdict(bool)

for y in range(m):
    line = list(map(int, input().split()))
    for x in range(n):
        positions[line[x]].append(x * y)


def end_find(end):
    todo = [end]
    while len(todo) > 0:
        cur = todo.pop(0)
        if cur == 1:
            return "yes"
        if done[cur] == False and positions[cur] != []:
            for k in positions:
                todo.append(k)
        done[cur] = True
    else:
        return "no"

print(end_find(m * n))
