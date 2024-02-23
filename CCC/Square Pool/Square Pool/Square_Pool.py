n = int(input())
t = int(input())

trees = [(-1, -1), (n, n)]


for k in range(t):
    x, y = map(int, input().split())
    trees.append((x - 1, y - 1))
    
x_s = sorted(trees, key = lambda x: x[0])
y_s = sorted(trees, key = lambda x: x[1])

max_sq = 0

if t == 0:
    print(n)
else:
    print(max_sq)
