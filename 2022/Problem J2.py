''' Fergusonball Ratings '''
N = int(input())
star = 0
for k in range(N):
    s = int(input())
    f = int(input())
    if ((s * 5) - (f * 3)) > 40:
        star += 1

if star == N:
    star = str(star) + "+"
print(star)
