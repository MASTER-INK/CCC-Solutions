N = int(input())
T = int(input())
trees = []
for l in range(T):
    tree = input()
    t_x, t_y = tree.split()
    t_x = int(t_x) - 1
    t_y = int(t_y) - 1
    trees.append([t_x, t_y])

def tree_check(cord, x, y, size):
    bot_x = x + size
    bot_y = y + size
    if ((cord[0] >= x and cord[0] <= bot_x) and (cord[1] >= y and cord[1] <= bot_y)):
        return False
    else:
        return True

def square_find(size):
    x = 0
    y = 0
    while y + size < N:
        while x + size < N:
            tree_c = None
            for cord in trees:
                if tree_c != False:
                    tree_c = tree_check(cord, x, y, size)
                else:
                    break
            if tree_c == True:
                return True
            x += 1
        x = 0
        y += 1
    return False



square_true = True
size = 0

while square_true:
    size += 1
    square_true = square_find(size)
print(size)
