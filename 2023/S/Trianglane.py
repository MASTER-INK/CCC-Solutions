#S1
def get_new_a(a):
    l = []
    for i in range(len(a) - 1):
        l.append(abs(a[i] - a[i + 1]))
    return l


n = 7
a = list(map(int, '3 1 4 1 5 9 2'.split()))

lowest = [0]
for i in range(n):
    a = get_new_a(a)
    lowest.append(min(a))
    print(a)
    print(*lowest)