from itertools import permutations
s = [1, 2, 3, 1, 2, 3]

print(list(permutations(s)))
t = 0
for p in list(permutations(s)):
    for i in range(5):
        if p[i] == p[i + 1]:
            break
    else:
        t += 1
print(t)