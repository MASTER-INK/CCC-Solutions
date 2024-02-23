'''Problem J4/S2: Good Groups'''
with open("inpts.txt") as namegroups:
    line = []
    for lines in namegroups:
        line.append(lines.strip())

def list_check(list, names, sep):
    conflicts = 0
    for n in list:
        if sep == False:
            if (n[0] in names and n[1] not in names) or (n[1] in names and n[0] not in names):
                list.remove(n)
            elif (n[0] in names and n[1] in names):
                conflicts += 1
        else:
            if (n[0] in names and n[1] in names):
                list.remove(n)
            elif (n[0] in names and n[1] not in names) or (n[1] in names and n[0] not in names):
                conflicts += 1
                list.remove(n)
    return conflicts

X = int(line[0])
together = []
for k in range(X):
    together.append(line[k + 1].split())


Y = int(line[X + 1])
seperate = []
for l in range(Y):
    seperate.append(line[Y + l].split())


G = int(line[X + Y + 2])
conflicts = 0
for m in range(1, G + 1, 1):
    names = line[X + Y + 2 + m].split()
    conflicts += list_check(together, names, True)
    conflicts += list_check(seperate, names, False)
print(conflicts)
