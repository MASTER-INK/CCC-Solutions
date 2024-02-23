###Problem J3: Cold Compress
import collections
N = int(input())
lines = collections.defaultdict(str)
for i in range(N):
    symb = collections.defaultdict(int)
    x = input()
    for l in x:
        symb[l] += 1
    lines[i] = symb

for j in lines:
    string = ""
    for l in lines[j]:
        string += (str(lines[j][l]) + " " + l + " ")
    print(string[:-1])
