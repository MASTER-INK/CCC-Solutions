import time

N = int(input())
T = int(input())
trees = []
line = []

for i in range(T):
    trees.append(input().split())

size = 1
starx = 0
stary = 0
highsize = []

while size < 5 and stary + starx < N * 2:
    pos = []
    for y in range(starx, size, 1):
        for x in range(stary, size, 1):
            l = [x, y]
            pos.append(l)
    print(pos)
    for j in pos:
        if j in trees:
            if starx < size:
                starx += 1
            else:
                starx = 0
                stary += 1
            highsize.append(size)
            size = 0
    size += 1


print(sorted(highsize), trees)
