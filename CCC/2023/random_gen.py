import random
n = 10
h = 10 


with open('input_text.txt', 'w') as inp:
    for i in range(n):
        num = random.randrange(h)
        inp.write(str(num) + " ")
