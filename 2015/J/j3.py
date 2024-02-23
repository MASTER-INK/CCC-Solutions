s = input()

vowels = ['a', 'e', 'i', 'o', 'u']
lets = list(map(lambda x: chr(x), [x for x in range(97, 123)]))

def next_ones(l):
    v = None
    c = None
    low_i = lets.index(l) - 1
    high_i = lets.index(l) + 1
    if l == 'z':
        c = 'z'
    while v == None or c == None:
        if low_i > -1:
            if v == None and lets[low_i] in vowels:
                v = lets[low_i]
            low_i -= 1
        if high_i < 26:
            if v == None and lets[high_i] in vowels:
                v = lets[high_i]
            if c == None and lets[high_i] not in vowels:
                c = lets[high_i]
            high_i += 1
    return v, c


new_s = ''

for l in s:
    if l not in vowels:
        v, c = next_ones(l)
    else:
        v, c = '', ''
    new_s += l + v + c
print(new_s)

