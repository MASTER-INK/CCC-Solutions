def sort_time(fre):
    return fre[1]
n = int(input())
### P = Initial pos
### Walk rate = 1 / W
### D = hearing range
friends = []
for i in range(n):
    friend = input().split()
    friends.append(friend)

def friend_run(list, tar):
    if int(list[0]) - int(list[2]) > tar:
        t = ((int(list[0]) - int(list[2])) - tar)
    else:
        t = (tar - (int(list[0]) + int(list[2])))
    return t * int(list[1])



C = 0
last_t = 0
t = 1

while t > last_t:
    last_t = t
    t = 0
    for k in friends:
        if k[0] != C:
            t += friend_run(k, C)
            print(t)
    C += 1
print(C)

print(t)
