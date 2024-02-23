d = int(input())

#12:34 = 00:34
sequences = ["34"]

for h in range(1, 12):
    for m in range(60):
        cur = str(h) + ('0' * (2 - len(str(m)))) + str(m)
        diff = int(cur[0]) - int(cur[1])
        for k in range(1, len(cur) - 1):
            if int(cur[k]) - int(cur[k + 1]) != diff:
                break
        else:
            mins = (h * 60) + m
            sequences.append(mins)
            
total = 0

total += (len(sequences) * ((d / 60) // 12))

left = d - (((d / 60) // 12) * 720)

x = 0
while left >= int(sequences[x]):
    x += 1
total += x
print(int(total))