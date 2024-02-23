"""n = 7
l = list(map(int, "3 1 4 1 5 9 2".split()))
"""

n = int(input())
l = list(map(int, input().split()))
sym = [0]

def get_asy(l):
    sum_l = 0
    for i in range(len(l) // 2):
        sum_l += abs(l[i] - l[(i + 1) * -1])
    return sum_l

for start in range(1, n):
    x = 0
    cur_min = None
    for y in range(start + 1, n + 1):
        new_a = get_asy(l[x:y])
        #print(new_a, l[x:y])
        if cur_min == None or new_a < cur_min:
            cur_min = new_a
        x += 1
    sym.append(cur_min)

print(*sym)