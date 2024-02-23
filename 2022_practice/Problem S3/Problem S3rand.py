import random
with open("Problem S3inputs.txt", "w") as p:
    n = random.randrange(0, 10)
    p.write(str(n) + "\n")
    for l in range(n):
        p.write(str(random.randrange(0, n)) + "\n")
