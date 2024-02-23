#n = int(input())

data = '''R 12
W 2
R 23
W 3
R 45
S 45
R 45
S 23
R 23
W 2
S 23
R 34
S 12
S 34'''.split('\n')

replies = {}
times = {}

pos = 0

for k in data:
    type, m = k.split()

    if type == 'W':
        pos += int(m)
    elif type != 'S':
        pos += 1

    if type == 'R':
        replies[m] = pos
        times[m] = -1
    elif type == 'S':
        if times[m] == -1:
            times[m] += 1
        times[m] += pos - replies[m]

    if type == 'S':
        pos += 1
    print(type, m, pos)

    
    
    
print(times)

