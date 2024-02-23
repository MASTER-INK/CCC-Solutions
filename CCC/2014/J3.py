# 3:54 min.
points = [100, 100]
for t in range(int(input())):
    a, d = map(int, input().split())
    
    if a < d:
        points[0] -= d
    elif d < a:
        points[1] -= a
        
for i in points:
    print(i)