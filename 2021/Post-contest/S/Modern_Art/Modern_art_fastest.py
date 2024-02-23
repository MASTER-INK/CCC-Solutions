import time
m = int(input())
n = int(input())
c = int(input())
g = []

for i in range(c):
    dire, place = input().split()
    place = int(place)
    if dire == "R":
        di = m
        for ce in range(di):
            pos = (place, ce)
            if pos not in g:
                g.append(pos)
            else:
                g.remove(pos)
    else:
        di = n
        for ce in range(di):
            pos = (ce, place)
            if pos not in g:
                g.append(pos)
            else:
                g.remove(pos)
print(g)
print(len(g))
