from collections import defaultdict

def group_add(groups, g):
    for m in range(3):
        groups[g[m] + " " + g[m - 1]] = True
        groups[g[m - 1] + " " + g[m]] = True
    return groups

constraints = {}

for x in range(int(input())):
    names = input()
    constraints[names] = True

for x in range(int(input())):
    names = input()
    constraints[names] = False
    
groups = defaultdict(bool)
for n in range(int(input())):
    g = input().split()
    groups = group_add(groups, g)

total = 0
#use a hasmap to perform a linear search on the groups dictionary.
for c in constraints:
    if constraints[c] != groups[c]:
        total += 1
print(total)