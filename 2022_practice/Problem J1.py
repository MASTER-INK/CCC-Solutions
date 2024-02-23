###Problem J1: What is n, Daddy?
n = int(input())
l = n
l2 = 0
if n > 5:
    l2 = n - 5
    l = 5

total = [sorted([l, l2])]
while l > 1 and l2 < 5:
    l -= 1
    l2 += 1
    k = sorted([l, l2])
    if k not in total:
        total.append(k)


print(len(total))
