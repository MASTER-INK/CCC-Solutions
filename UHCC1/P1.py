x, y, z = map(int, input().split())

l = int(input())

p1 = 0
p2 = 0

while p1 < l and p2 < l:
    if p1 < p2:
        p1 += x
    else:
        p1 += z
        p2 += y

if p2 >= l:
    print(2)
else:
    print(1)