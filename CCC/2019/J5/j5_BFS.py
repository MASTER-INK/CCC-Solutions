import collections
"""rules = {}

for i in range(3):
    cur = input().split())
    rules[cur[0]] = cur[1]
t, start, end = input().split()"""

rules = {"AA":"AB", "AB": "BB","B": "AA"}

t, current, end = 1, "AB", "AAAB"

todo = collections.defaultdict(list)

todo[t] = [[current, [0]]]

print("go")

while t > 0:
    for subs in range(len(todo[t])):
        current = todo[t][subs][0]
        for rule in rules:
            for i in range((len(current) - len(rule)) + 1):
                print(rule, current[i:i + len(rule)], i)
                if rule == current[i:i + len(rule)]:
                    todo[t - 1].append([])
    t -= 1
    
       