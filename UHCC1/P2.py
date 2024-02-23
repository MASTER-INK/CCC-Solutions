from collections import defaultdict
"""
k = int(input())
s = input()
n = int(input())
w_list = []
for j in range(n):
    w_list.append(input())
    """
k = 8
s = "aabcdefg"
n = 4
w_list = ["aa", "abc", "def", "ef"]
pos_dict = defaultdict(bool)

total = 0
for w in w_list:
    f = s.find(w)
    while f != -1:
        for k in range(len(w)):
            if pos_dict[k + f] == True:
                total += 1
            else:
                pos_dict[k + f] = True
        f = s[f + 1:].find(w)
print(total)