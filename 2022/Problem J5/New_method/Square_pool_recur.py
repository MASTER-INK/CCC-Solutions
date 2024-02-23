import numpy as np
import time
def square_pool():
    N = int(input())
    T = int(input())
    trees = []

    for i in range(T):
        trees.append(input().split())

    def new_moves(pos, xtrue, x, y, new_negative):
        types = [1 * pos, 1 * pos]
        if new_negative and pos == -1:
            types = [1 * pos, 0]
        elif new_negative and pos == 1:
            types = [0, 1 * pos]
        elif new_negative == False and xtrue == False:
            if pos == -1:
                types = [1, 1 * pos]
            else:
                types = [1 * -1, 1 * -1]
        elif new_negative == False and xtrue:
            if pos == 1:
                types = [1, 1]
            else:
                types = [1, -1]
        if xtrue == True:
            new_pos = x + types[0], y + types[1]
        else:
            new_pos = x + types[1], y + types[0]
        return new_pos
    def move_calc(place_list):
        new_place_list = []
        for numbers_list in place_list:
            x, y = int(numbers_list[0]), int(numbers_list[1])
            pos_times = [1, 3, 5, 7]
            xtrue_times = [0, 1, 4, 5]
            new_negative_times = [0, 1, 2, 3]
            for tk in range(8):
                if tk in pos_times:
                    pos = 1
                else:
                    pos = -1
                if tk in xtrue_times:
                    xtrue = True
                else:
                    xtrue = False
                if tk in new_negative_times:
                    new_negative = True
                else:
                    new_negative = False
                new_x, new_y = new_moves(pos, xtrue, x, y, new_negative)
                print(new_x, new_y)
                print(pos)
                """if new_x >= 0 and new_y >= 0:
                    if new_x < len(grid) and new_y < len(grid) and grid[new_x][new_y] == ".":
                        grid[new_x][new_y] = " "
                        ps = new_x, new_y
                        if ps not in place_list:
                            new_place_list.append(ps)"""
        return new_place_list
    print(move_calc(trees))
if __name__ == "__main__":
    square_pool()
