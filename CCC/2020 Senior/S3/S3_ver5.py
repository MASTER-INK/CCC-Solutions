from collections import defaultdict

# ver1 add the last letter, remove first, count collections
# ver2 a bit faster. Skips all if new letter added is not in N at all.


def dict_check(d_h, d_n, last):
    if last[0] == False:
        for l in list(d_n):
            if d_h[l] != d_n[l]:
                return False
    else:
        if d_h[last[1]] != d_n[last[1]]:
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

found_needles = 0

new_let = None
last_dict_good = False 

while c <= len(h):
    ##print(c, dict_h, dict_n, dict_found, h[c - len(n):c])
    if dict_check(dict_h, dict_n, (last_dict_good, new_let)) == True and dict_found[h[c - len(n):c]] == False:
        found_needles += 1
        dict_found[h[c - len(n):c]] = True
        last_dict_good = True
    else:
        last_dict_good = False
        
    if c != len(h):
        dict_h[h[c - len(n)]] -= 1
        dict_h[h[c]] += 1
        new_let = h[c]
    c += 1
print(found_needles)
