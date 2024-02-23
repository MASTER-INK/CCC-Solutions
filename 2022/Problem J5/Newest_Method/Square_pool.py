N = int(input())
T = int(input())
trees = []
grid = [[""] * N for i in range(N)]
for l in range(T):
    tree = input()
    x, y = tree.split()
    x = int(x) - 1
    y = int(y) - 1
    trees.append([x, y])
    grid[x][y] = "T"

for n in grid:
    print(n)

def square_find(size):
    x = 0
    y = 0
    new_grid = grid

    while y + (size - 1) < N:
        while x + (size - 1) < N:
            sq = True
            new_grid[x][y] = "x"
            new_grid[x + (size - 1)][y + (size - 1)] = "x"
            for n in new_grid:
                print(n)
            print()
            for cord in trees:
                if (int(cord[0]) > x + (size - 1) and int(cord[1]) > y + (size - 1)) or (int(cord[0]) < x and int(cord[1]) > y + (size - 1)) or (int(cord[0]) > x + (size - 1) and int(cord[1]) < y) or (int(cord[0]) < x and int(cord[1]) < y):
                    print(x, y)
                    sq = True
                else:
                    sq = False
                    break
            new_grid = [[""] * N for i in range(N)]
            if sq:
                return True
            x += 1
        y += 1
        x = 0
    return False



square_true = True
size = 0

while square_true:
    size += 1
    square_true = square_find(size)
    print(size)
