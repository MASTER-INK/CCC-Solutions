
from S3 import get_good_samples
from collections import defaultdict

def col_check(l_list, col):
    for p in l_list:
        if col[p] > 1:
            return False
    return True

def check_sample(l, n):
    total = 0
    for r in range(1, n):
        col = defaultdict(int)
        large_list = []
        for k in range(r):
            col[l[k]] += 1
        non_set = False
        for f in col:
            if col[f] > 1:
                large_list.append(f)
                non_set = True
        if non_set == False:
            total += 1
        for j in range(r, n):
            col[l[j - r]] -= 1
            col[l[j]] += 1
            if col[l[j - r]] <= 1 and l[j - r] in large_list:
                large_list.remove(l[j - r])
            if col[l[j]] > 1 and l[j] not in large_list:
                large_list.append(l[j])
            if col_check(large_list, col) == True:
                total += 1
        print("R:", r)
    print(total)
    return total

n, m, k = 999996, 465582, 15518494024
l = get_good_samples(n, m, k)
if len(l) == n and check_sample(l, n) == k:
    print(True)
else:
    print(False)