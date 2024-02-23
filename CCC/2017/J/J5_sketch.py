from itertools import combinations
import collections

n = int(input())

a = map(int, input().split())


col = collections.defaultdict(int)

max_l = 0

for k in combinations(a, 2):
    cur = sum(k)
    col[cur] += 1
    if col[cur] > max_l:
        max_l = col[cur]

x = 0

new_col = sorted(col, key = lambda x : col[x], reverse=True)

while x < len(new_col) and col[new_col[x]] == max_l:
    x += 1

print(max_l, x)


"""

os.chdir("C:\\Users\\rmath\\Visual Code\\CCC\\2017\\J\\j5")

file_n = "j5.03"



with open(file_n + ".in") as data:
    n = None
    for line in data:
        if n == None:
            n = line.strip()
        else:
            a_list = list(map(int, line.strip().split()))
        

#n = int(input())

#a_list = list(map(int, input().split()))

woods = collections.defaultdict(int)

ways = collections.defaultdict(int)

for i in a_list:
    woods[i] += 1
    
for k in range(len(woods)):
    for p in range(k, len(woods)):
        a = list(woods)[k]
        b = list(woods)[p]
        #print(a, b)
        #print(k, p)
        if k == p:
            ways[a + b] += woods[a] // 2
        else:
            ways[a + b] += min(woods[a], woods[b])
        #print(ways, woods, len(woods))

m = sorted(ways, key = lambda x: ways[x], reverse = True)

high = ways[m[0]]

diff_high = 0
#print(m, ways)
while ways[m[diff_high]] == high:
    diff_high += 1
my_ans = "".join(str(high) + " " + str(diff_high))

with open(file_n + ".out") as end_p:
    ans = ""
    for k in end_p:
        ans = k.strip()
        
print(ans, my_ans)
        
print(ans == my_ans)
        
    

"""
