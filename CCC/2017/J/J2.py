n = int(input())

k = int(input())

total = 0
for i in range(k + 1):
    total += n * (10 ** i)
print(total)

#find formula later