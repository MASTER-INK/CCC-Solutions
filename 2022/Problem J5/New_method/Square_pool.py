import numpy as np
import time
N = int(input())
T = int(input())
trees = []

for i in range(T):
    trees.append(input().split())

def tree_area_ck(tree, valx, valy, N):
    y, x = tree
    square_pos = [x, y]
    if valx < 0:
        x -= 1
    else:
        x += 1
    if valy < 0:
        y -= 1
    else:
        y += 1
    square_size = 0
    while x > 0 and y > 0 and x < N and y < N:
        y -= valy
        x -= valx
        square_size += 1
    square_pos = square_pos, [x, y]
    return square_size, square_pos

values = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
squares = []
for tree in trees:
    tree = [int(tree[0]), int(tree[1])]
    for p in values:
        squares.append(tree_area_ck(tree, p[0], p[1], N))
print(sorted(squares))
