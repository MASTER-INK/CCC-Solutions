###https://dmoj.ca/problem/coci22c4p1
import collections

"""n, m = map(int, input().split())

s = list(input())"""

n, m = 6, 4

s = "orkddk"

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

#print(todo)

bonus = round(min(todo) - 0.1)

##print(bonus)

while m > 0:
    to_get_to = round(min(todo) - 0.1) + 1
    total_points = 7
    to_add = 0
    sum_m = 0
    broke = False
    #print(col_s)
    old = col_s.copy()
    for x in range(len(reqs)):
        let = list(reqs)[x]
        if todo[x] < to_get_to:
            to_add += ((to_get_to - todo[x]) * reqs[let])
            col_s[let] += ((to_get_to - todo[x]) * reqs[let])
            total_points += ((((to_get_to * reqs[let]) ** 2) -
                             (((to_get_to * reqs[let]) - 1) ** 2)))
            if m - to_add < 0:
                col_s = old
                broke = True
                ##print("Break")
                break
            todo[x] = to_get_to
    else:
        sum_m += total_points
        new_m = m - to_add
        print(new_m)
        max_points = ((((m_x[0] + 1) ** 2) - ((m_x[0]) ** 2)) * to_add) + (2 * (to_add // 2))
        print("m", max_points, to_add, sum_m)
        if sum_m <= max_points:
            col_s = old
            broke = True
        else:
            for k in col_s:
                if col_s[k] > m_x[0]:
                    m_x = (col_s[k], k)
            m -= to_add
            bonus += 1
        
    if broke == True:
        col_s[m_x[1]] += m
        m = 0
    ###print(sum_m, broke, m, col_s)
#print(col_s)
#print(sum_m)
#print(max_points)

points = 0


for j in col_s:
    points += (col_s[j] ** 2)
    
points += (7 * bonus)

print(int(points))