n, d = map(int, input().split())

l = list(map(int, input().split()))
bombs = 0
chain = 0
max_chain = 0
for i in range(n - 1):
    if abs(l[i + 1] - l[i]) <= d:
        chain += 1
    else:
        bombs += 1
        if chain > max_chain:
            max_chain = 0 + chain
        chain = 0
print(bombs + 1)
print(max(max_chain, chain) + 1)