n = int(input())
t = int(input())

sq = [['x' for x in range(n)] for y in range(n)]
trees = [(-1, -1), (n, n)]


for k in range(t):
    x, y = map(int, input().split())
    sq[x - 1][y - 1] = 'T'
    trees.append((x - 1, y - 1))
    
#print(trees)
#for l in sq:
    #print(*l)
    
def tree_check(pos_1, pos_2):
    for t_p in trees:
        if min(pos_1[0], pos_2[0]) <= t_p[0] <= max(pos_1[0], pos_2[0]) and min(pos_1[1], pos_2[1]) <= t_p[1] <= max(pos_1[1], pos_2[1]):
            return False
    return True
    
def sq_check(max_sq, cur_pos):
    pos = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
    moves = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
    for p in pos:
        s_x = cur_pos[0] + p[0]
        s_y = cur_pos[1] + p[1]
        if 0 <= s_x < n and 0 <= s_y < n: 
            for m in moves:
                m_x = s_x + (m[0] * max_sq)
                m_y = s_y + (m[1] * max_sq)
                #print(max_sq, (s_x, s_y), (m_x, m_y), m)
                #check next size
                while (0 <= m_x < n and 0 <= m_y < n) and tree_check((s_x, s_y), (m_x, m_y)):
                    max_sq += 1
                    m_x += m[0]
                    m_y += m[1]
                    #print(max_sq, (m_x, m_y))
                #print('BREAK')
                    
    return max_sq

max_sq = 0
for t_r in trees:
    max_sq = sq_check(max_sq, t_r)

if t == 0:
    print(n)
else:
    print(max_sq)