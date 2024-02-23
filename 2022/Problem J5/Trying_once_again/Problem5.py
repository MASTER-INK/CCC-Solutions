import collections

def tree_importer(file):
    trees = []
    sq = True
    with open(file) as ins:
        for line in ins:
            if sq == True:
                size = int(line.strip())
                sq = False
            else:
                t = line.strip().split()
                if len(t) > 1:
                    t = (int(line.strip().split()[0]), int(line.strip().split()[1]))
                    print(t)
                    trees.append(t)
    return trees, size

###func for creating boxes from each of those points
def box_expander(list_pos, size):
    ###helper func for bad_tree_pos
    def bad_tree_find(p, n, x, y):
        ### very small func to stop repition:
        def bad_t(p, n, val, x):
            n_p = p
            print(n)
            for k in range(n):
                print("k", k)
                if x == True:
                    n_p = [n_p[0] + (val * k), n_p[1]]
                else:
                    n_p = [n_p[0], n_p[1] + (val * k)]
                print(n_p, end = "")
                if n_p in bad_pos:
                    return False
            return True

        one_x = bad_t(p, n, x, True)

        two_y = bad_t(p, n, y, False)

        return (one_x and two_y)



    box_sizes = []
    for p in list_pos:
        for x in range(-1, 2, 2):
            for y in range(-1, 2, 2):
                n = 0
                c_box = []
                new_p = (p[0] + (x * n), p[1] + (y * n))
                while (size > new_p[0] > 1 and size > new_p[1] > 1) and bad_tree_find(new_p, n, x, y):
                    new_p = (p[0] + (x * n), p[1] + (y * n))
                    c_box.append(new_p)
                    n += 1
                box_sizes.append(len(c_box))
    return box_sizes




###func for all pos around a tree
def tree_around_finder(pos, size):
    new_list = []
    ### 9 different ways the box can be around the tree.
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            new_pos = (pos[0] + x, pos[1] + y)
            if (size >= new_pos[0] > 0 and size >= new_pos[1] > 0) and new_pos not in bad_pos:
                print("n", new_pos)
                new_list.append(new_pos)
    return new_list

###func to combine both tree_around_finder and box_expander
def box_tree(pos, size):

    t_around = tree_around_finder(pos, size)

    boxes_size = box_expander(t_around, size)

    boxes_size.sort(reverse = True)

    print()

    print(boxes_size)

    return boxes_size[0]




trees, size = tree_importer("input.txt")

globals()["bad_pos"] = trees

print("t", trees)

print(box_tree(trees[0], size))
grid = ""
