'''Problem J4/S2: Good Groups'''
with open("inpts.txt") as namegroups:
    line = []
    for lines in namegroups:
        line.append(lines.strip())

X = int(line[0])
together = []
for k in range(X):
    together.append(line[k + 1].split())


Y = int(line[X + 1])
seperate = []
for l in range(0, Y, 1):
    seperate.append(line[X + Y + l].split())


G = int(line[X + Y + 2])
conflicts = 0
ids = [1, 0]
for m in range(1, G + 1, 1):
    names = line[X + Y + 2 + m].split()
    for m in names:
        for c in together:
            if (m in c and c[ids[c.index(m)]] not in names):
                print(m,  c[ids[c.index(m)]])
                conflicts += 1
                together.remove(c)
        for d in seperate:
            if (m in d and d[ids[d.index(m)]] in names):
                print(m,  d[ids[d.index(m)]])
                conflicts += 1
                seperate.remove(d)


print(conflicts)
