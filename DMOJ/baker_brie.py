# https://dmoj.ca/problem/ecoo17r3p1

t = 10

for _ in range(t):
    f, d = map(int, input().split())
    
    cur_bonus = 0
    cur_f = [0 for i in range(f)]
    
    for i in range(d):
        day = list(map(int, input().split()))
        
        if sum(day) % 13 == 0:
            cur_bonus += sum(day) // 13
            
        for y in range(f):
            cur_f[y] += day[y]
    
    for x in cur_f:
        if x % 13 == 0:
            cur_bonus += x // 13
    print(cur_bonus)
    