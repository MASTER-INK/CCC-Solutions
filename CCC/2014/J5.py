# done in 10:32 min.
# easiest J5 of my life.
n = int(input())

names_dict = {}

a = input().split()

b = input().split()

for i in range(n):
    if a[i] in list(names_dict):
        if b[i] != names_dict[a[i]]:
            print("bad")
            break
    elif b[i] in list(names_dict):
        if a[i] != names_dict[b[i]]:
            print("bad")
            break
    else:
        if b[i] == a[i]:
            print("bad")
            break
        names_dict[a[i]] = b[i]
else:
    print("good")
