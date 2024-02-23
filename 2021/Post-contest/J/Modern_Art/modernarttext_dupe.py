import time
with open("Modern_inputs.txt") as input_numbs:
    file_inp = []
    for i in input_numbs:
        file_inp.append(i.strip())


m = int(file_inp[0])
n = int(file_inp[1])
k = int(file_inp[2])
g = []

while k > 0:
    dire, place = file_inp[(len(file_inp) - k)].split()
    place = int(place) - 1
    if dire == "R":
        di = n
        for ce in range(di):
            pos = (place, ce)
            if pos not in g:
                g.append(pos)
            else:
                g.remove(pos)
    else:
        di = m
        for ce in range(di):
            pos = (ce, place)
            if pos not in g:
                g.append(pos)
            else:
                g.remove(pos)
    k -= 1
print(len(g))
print(time.process_time())
