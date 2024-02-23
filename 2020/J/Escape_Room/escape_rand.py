import random
with open("escape.txt.txt", "w") as he:
    lets = ["R", "C"]
    for i in range(2):
        num = str(random.randrange(0, 100))
        he.write(num + "\n")
        if i == 0:
            row_num = num
        elif i == 1:
            col_num = num
    for d in range(int(row_num)):
        for l in range(int(col_num)):
            j = random.randrange(0, 100)
            he.write(str(j) + " ")
        he.write("\n")
