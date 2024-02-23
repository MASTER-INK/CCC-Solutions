from math import pow, ceil, floor
def mult(l):
    x = 1
    for i in l:
        x *= i
    return x

"""def find_max(n, m):
    print(n % m)
    lowest_l = []
    val = n // m
    for i in range(m):
        if n % m >= i:
            lowest_l.append(val + 1)
        else:
            lowest_l += [val for x in range(m - i)]
            break
    return lowest_l"""
    
def find_max(n, m):
    lowest_l = []
    val = pow(n, 1 / m)
    i_val = int(val)
    print(val, n, m)
    cur_av = 0
    for i in range(1, m + 1):
        if cur_av < val:
            cur_av += (((i_val + 1) - cur_av) / i)
            lowest_l.append(i_val + 1)
        else:
            cur_av += (((i_val) - cur_av) / i)
            lowest_l.append(i_val)
    print(cur_av, i_val)
    return lowest_l
    
def find_next(l):
    new_l = []
    for i in range(len(l)):
        if l[i] == 8:
            new_l.append(1)
        else:
            new_l.append(l[i] + 1)
            new_l += l[i + 1:]
            break
    else:
        return False
    return new_l

l_1 = [1 for i in range(5)]
l_2 = [1 for i in range(3)]
next = True

print(find_max(48, 3))

while next == True:
    print()
    next = False