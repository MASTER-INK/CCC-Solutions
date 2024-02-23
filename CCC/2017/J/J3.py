def diff(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def make_it(start, end, d, charge):
    cur = charge - d
    if cur == 0:
        return "Y"
    if cur > 0:
        if cur % 2 == 0:
            return "Y"
        else:
            return "N"
    else:
        return "N"
        
    

start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))
charge = int(input())

d = diff(start, end)

print(make_it(start, end, d, charge))