import random
import string

s = []

for i in range(15):
    s.append(random.choice(list(string.ascii_letters) + list(string.printable)))
    
print("".join(s))