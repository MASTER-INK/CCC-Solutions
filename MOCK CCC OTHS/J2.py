n = int(input())

l = []
for j in range(n):
    l.append(int(input()))
l.sort()
print(sum(l[:-1]) // (n - 1))