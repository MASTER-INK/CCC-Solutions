'''Problem J4/S2: Good Groups'''
import collections
with open("inpts.txt") as namegroups:
    line = []
    for lines in namegroups:
        line.append(lines.strip())

X = int(line[0])
together = collections.defaultdict(list)
for k in range(X):
    o, t = line[k + 1].split()
    together[o] += t


Y = int(line[X + 1])
seperate = collections.defaultdict(list)
for l in range(0, Y, 1):
    o, t = line[k + 1].split()
    seperate[o] += t
    print(o, t)

conflicts = 0
def list_check(names, list, tog):
    conflicts = 0
    for m in names:
        if len(list[m]) > 0:
            print(list[m], "let:", m, names)
            for l in list[m]:
                if tog == True:
                    if l not in names:
                        conflict += 1
                else:
                    if l in names:
                        conflict += 1
    return conflicts

G = int(line[X + Y + 2])
for m in range(1, G + 1, 1):
    names = line[X + Y + 2 + m].split()
    conflicts += list_check(names, together, True)
    conflicts += list_check(names, seperate, False)


print(conflicts)
