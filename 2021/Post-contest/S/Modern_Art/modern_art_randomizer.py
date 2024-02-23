import random
with open("Modern_inputs.txt", "w") as he:
    lets = ["R", "C"]
    for i in range(3):
        num = str(random.randrange(0, 2200))
        if i == 2:
            num = str(random.randrange(0, 1000))
        he.write(num + "\n")
        if i == 0:
            row_num = num
        elif i == 1:
            col_num = num
        else:
            input_num = num
    for d in range(int(input_num)):
        let_let = lets[random.randrange(0, 2)]
        if let_let == "R":
            num = random.randrange(0, int(row_num))
        else:
            num = random.randrange(0, int(col_num))
        he.write(let_let + " " + str(num) + "\n")
