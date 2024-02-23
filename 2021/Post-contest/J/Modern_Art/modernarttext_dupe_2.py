import time
with open("Modern_inputs.txt") as input_numbs:
    file_inp = []
    for i in input_numbs:
        file_inp.append(i.strip())


m = int(file_inp[0])
n = int(file_inp[1])
k = int(file_inp[2])
g = []
g2 = []

while k > 0:
    dir, plac = file_inp[(len(file_inp) - k)].split()
    let = (dir, (int(plac) - 1))
    if let not in g2:
        g2.append(let)
    elif let in g2:
        g2.remove(let)
    k -= 1

for nums in g2:
    dire = nums[0]
    place = nums[1]
    if dire == "R":
        for ce in range(n):
            pos = (int(ce), int(place))
            if pos not in g:
                g.append(pos)
            else:
                g.remove(pos)
    else:
        for ce in range(m):
            pos = (int(place), int(ce))
            if pos not in g:
                g.append(pos)
            else:
                g.remove(pos)
print(len(g))
print(time.process_time())
