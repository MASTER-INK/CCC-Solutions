# 15:34 min 
# hardest one lol

sides = []
for i in range(3):
    sides.append(int(input()))
if sum(sides) != 180:
    print("Error")
else:
    e = 0
    for i in range(3):
        if sides[i] == sides[i- 1]:
            e += 1
    if e == 3:
        print("Equilateral")
    elif e == 1:
        print("Isosceles")
    else:
        print("Scalene")

