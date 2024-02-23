###Problem S3: Absolutely Acidic
import collections
def sec_key(i):
    return readings[i], i
n = int(input())
readings = collections.defaultdict(int)
for i in range(n):
    readings[int(input())] += 1

op = []
for l in sorted(readings, key = sec_key):
    if len(op) >= 2:
        break
    if readings[l] not in op:
        op.append(readings[l])
if len(op) < 2:
    print(abs(sorted(readings, key = sec_key)[-1] - sorted(readings, key = sec_key)[0]))
else:
    if len(sorted(readings, key = sec_key)) > 2:
        l = -2
        l2 = -1
        larg = [sorted(readings, key = sec_key)[-1], sorted(readings, key = sec_key)[-2]]
        for i in range(2):
            while readings[sorted(readings, key = sec_key)[l2]] == readings[sorted(readings, key = sec_key)[l]] and abs(l) < len(sorted(readings, key = sec_key)):
                l -= 1
                larg.append(sorted(readings, key = sec_key)[l])
            l2 = l
    else:
        l = -2
        larg = [sorted(readings, key = sec_key)[-1]]
        while readings[sorted(readings, key = sec_key)[-1]] == readings[sorted(readings, key = sec_key)[l]]:
            l -= 1
            larg.append(sorted(readings, key = sec_key)[l])
    print(sorted(larg)[-1] - sorted(larg)[0])
