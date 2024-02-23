'''Problem J4/S2: Good Groups'''

X = int(input())
together = []
for k in range(X):
    together.append(input().split())

Y = int(input())
seperate = []
for l in range(Y):
    seperate.append(input().split())

G = int(input())
conflicts = 0
ids = [1, 0]
for m in range(G):
    names = input().split()
    for m in names:
        for c in together:
            if (m in c and c[ids[c.index(m)]] not in names):
                conflicts += 1
            together.remove(c)
        for d in seperate:
            if (m in d and d[ids[d.index(m)]] in names):
                conflicts += 1
            seperate.remove(d)
print(conflicts)
