import random
import string
with open("inpts.txt", "w") as he:
    for i in range(3):
        num = str(random.randrange(0, 22))
        if i == 2:
            num = str(random.randrange(0, 10))
        he.write(num + "\n")
        let = ""
        if i == 0:
            row_num = num
            for m in range(int(num)):
                let = ""
                for l in range(2):
                    let += random.choice(list(string.ascii_uppercase)) + " "
                he.write(let + "\n")
        elif i == 1:
            col_num = num
        else:
            input_num = num
