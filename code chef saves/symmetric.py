
#l = [3, 1, 4, 1, 5, 9, 2]
most_sym = []

#n = len(l)

n = int(input())

l = list(map(int, input().split()))

def calc_sum(lis, s):
    t_sum = 0
    for k in range(len(lis) // 2):
        t_sum += abs(lis[k] - lis[s - (k + 1)])
    #print(t_sum)
    return t_sum

for s in range(1, n + 1):
    cur_lowest = None
    
    for i in range((n - s) + 1):
        lis = l[i:s + i]
        cur_sum = calc_sum(lis, s)
        if cur_lowest == None or cur_sum < cur_lowest:
            cur_lowest = cur_sum
    most_sym.append(cur_lowest)
print(*most_sym)