###Problem J1: Winning Score
teams = [0, 0]
for p in range(2):
    for k in range(3):
        teams[p] += (3 - k) * int(input())

print("A" if teams[0] > teams[1] else "B" if teams[1] > teams[0] else "T")
