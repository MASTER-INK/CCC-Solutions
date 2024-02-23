def sort_time(fre):
    return fre[1]

def sort_time2(fre):
    return tar - fre
n = int(input())
### P = Initial pos
### Walk rate = 1 / W
### D = hearing range
friends = []
for i in range(n):
    friend = input().split()
    friends.append(friend)

def friend_run(list, tar):
    ke = [int(list[0]) - int(list[2]), int(list[0]) + int(list[2])]
    m = []
    for l in ke:
        m.append(l)
    print(sorted(m, key = sort_time2))
    return t * int(list[1])



C = 0
x = 0
t = 0

while x < 50:
    last_t = t
    t = 0
    for k in friends:
        if k[0] != C:
            t += friend_run(k, C)
    print(t, C)
    C += 1
    x += 1
print(t)
