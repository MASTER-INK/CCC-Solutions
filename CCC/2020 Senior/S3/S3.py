from collections import defaultdict

#ver1 add the last letter, remove first, count collections

def dict_check(d_h, d_n):
    for l in list(d_n):
        if d_h[l] != d_n[l]:
            return False
    return True

#n = "aab"

#h = "abacabaa"

n = input()

h = input()

dict_n = defaultdict(int)

dict_h = defaultdict(int)

dict_found = defaultdict(bool)

for let in n:
    dict_n[let] += 1
    
c = len(n)
    
for let in h[:c]:
    dict_h[let] += 1
    
cur_perm = h[:c]
found_needles = 0

while c <= len(h):
    ##print(c, dict_h, dict_n, dict_found, h[c - len(n):c])
    if dict_check(dict_h, dict_n) == True and dict_found[h[c - len(n):c]] == False:
        found_needles += 1
        dict_found[h[c - len(n):c]] = True
    if c != len(h):
        dict_h[h[c - len(n)]] -= 1
        dict_h[h[c]] += 1
    c += 1    
print(found_needles)