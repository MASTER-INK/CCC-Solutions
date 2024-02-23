#Modern art ccc 2021
from collections import defaultdict

brush = {'R': defaultdict(bool),
         'C': defaultdict(bool)}

total = {'R': 0,
         'C': 0}

m = int(input())
n = int(input())

for k in range(int(input())):
    t, num = input().split()
    brush[t][num] = not brush[t][num]
    if brush[t][num] == True:
        total[t] += 1
    else:
        total[t] -= 1

gold = (total['R'] * (n - total['C'])) + (total['C'] * (m - total['R']))
print(gold)