n = int(input())
p = []
y = []
for l in range(n):
    X, Y = input().split(",")
    p.append(int(X))
    y.append(int(Y))

print(str(sorted(p)[0] - 1) + "," + str(sorted(y)[0] - 1))
print(str(sorted(p)[-1] + 1) + "," + str(sorted(y)[-1] + 1))
