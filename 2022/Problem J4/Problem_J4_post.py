import numpy as np
X = int(input())
not_n = []
yes_n = []
for k in range(X):
    names = input().split()
    not_n.append(names)
Y = int(input())
for d in range(Y):
    names = input().split()
    yes_n.append(names)

print(not_n, yes_n)
G = int(input())
for v in range(G):
    group = input().split()
    for l in group:
        print(l)
