###Problem S1: Sum Game
N = int(input())
Sw = input().split()
Sm = input().split()
days = [0]
total = 0
for l in range(1, N + 1, 1):
    total -= int(Sw[l - 1]) - int(Sm[l - 1])
    if total == 0 and l != 1:
        days.append(l)
print(sorted(days)[-1])
