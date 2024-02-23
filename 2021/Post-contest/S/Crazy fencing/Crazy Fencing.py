N = input()
H = input().split()
W = input().split()

total = 0
for i in range(len(W)):
    total += int(W[i]) * ((int(H[i]) + int(H[i + 1])) / 2)
print(total)
