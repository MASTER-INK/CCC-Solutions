###https://dmoj.ca/problem/coci22c4p1
import collections

"""n, m = map(int, input().split())

s = list(input())"""

n, m = 15, 0

s = "ddkkoorrkdrkoorkk"

col_s = collections.defaultdict(int)

reqs = {"k": 2,
        "r": 1,
        "o": 2,
        "d": 1}

m_x = (0, None)

for i in s:
    col_s[i] += 1
    
    if col_s[i] > m_x[0]:
        m_x = (col_s[i], i)
        
todo = [0, 0, 0, 0]

for let_pos in range(len(reqs)):
    let = list(reqs)[let_pos]
    todo[let_pos] = col_s[let] / reqs[let]
    
to_reach_next = []

print(todo)

for i in range(7):
    to_get_to = round(min(todo) - 0.1) + 1
    to_add = 0
    for x in range(len(reqs)):
        let = list(reqs)[x]
        if todo[x] < to_get_to:
            to_add += ((to_get_to - todo[x]) * reqs[let])
            todo[x] = to_get_to
    to_reach_next.append(to_add)
print(to_reach_next)

if m_x[0] >= 7:
    print("max", m_x)
    col_s[m_x[1]] += m
else:
    print("do add")