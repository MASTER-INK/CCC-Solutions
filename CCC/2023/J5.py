s = list(input())
n_y = int(input())
n_x = int(input())

a = []
start_todo = []

for y in range(n_y):
    line = input().split()
    for x in range(n_x):
        if line[x] == s[0]:
            start_todo.append([x, y])
    a.append(line)


def perp_true(diff, direct):
    if 0 in direct and 0 in diff:
        return True
    elif 0 not in direct and 0 not in diff:
        return True
    else:
        return False


def direct_check(old_pos, pos, second_l, direct):
    diff = [old_pos[0] - pos[0], old_pos[1] - pos[1]]
    if direct == None:
        return pos, False, diff, True
    else:
        if diff == direct:
            return pos, second_l, direct, True
        elif second_l == False and diff != direct and perp_true(diff, direct) == True:
            return pos, True, diff, True
        else:
            return pos, True, direct, False


def around_finder(pos, let_pos, done_list, second_l, direct):
    x_lis = [1, 0, -1]
    y_lis = [1, 0, -1]
    next_lis = []
    good = False
    for x in x_lis:
        for y in y_lis:
            if x != 0 or y != 0:
                new_pos = (pos[0] + x, pos[1] + y)
                if (0 <= new_pos[0] < n_x and 0 <= new_pos[1] < n_y) and (new_pos not in done_list):
                    if a[new_pos[1]][new_pos[0]] == s[let_pos]:
                        new_pos, new_second_l, new_direct, good = direct_check(
                            pos, new_pos, second_l, direct)
                        if good == True:
                            next_lis.append(
                                (new_pos, let_pos + 1, new_second_l, new_direct))
    return next_lis


total_words = 0
done_list = []
while len(start_todo) > 0:
    start = start_todo.pop(0)
    todo = around_finder(start, 1, [], None, None)
    done_list += todo
    while len(todo) > 0:
        cur = todo.pop(0)
        if cur[1] == len(s):
            total_words += 1
        else:
            new_list = around_finder(cur[0], cur[1], done_list, cur[2], cur[3])
            todo += new_list
            done_list += new_list
print(total_words)
