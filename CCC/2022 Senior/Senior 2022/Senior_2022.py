from math import floor
def get_ways(n):
    low = n / 4
    if low != int(low):
        fours = floor(low) - int((low - floor(low)) * 3)
        if fours < 0:
            fours = (n - (floor(low) * 4))
    else:
        fours = floor(low)
        
    print(fours)
    if fours < 0:
        return 0
    else:
        return int(fours // 3)
    
for n in range(100):
    print(n, get_ways(n))