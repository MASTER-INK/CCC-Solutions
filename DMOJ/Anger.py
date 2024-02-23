from collections import defaultdict
n = int(input())

a = defaultdict(int)
b = defaultdict(int)

a_ind = {}
b_ind = {}

v_a = 1
v_b = 1
found = False

while found == False:
    print(v_a, v_b)
    cur_a, cur_b = map(int, input().split())
    a_ind[cur_a] = v_a
    b_ind[cur_b] = v_b
    a[cur_a] = True
    b[cur_b] = True
    if b[cur_a] == True or a[cur_b] == True:
        found_num = cur_a
        found = True
    else:
        v_a += 1
        v_b += 1
print(b_ind[found_num], a_ind[found_num])
cur_a, cur_b = map(int, input().split())
