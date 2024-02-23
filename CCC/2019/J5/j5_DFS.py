import collections
"""
rules = {}
for i in range(3):
    cur = input().split()
t, start, end = input().split()"""

rules = {
    "AA": "AB",
    "AB": "B",
    "B": "AA"
}

times, start, end = 4, "AB", "AAAB"

def go_current_switch(cur, r):
    global done
    for rule_n in range(len(rules)):
        l_rule = list(list(rules)[rule_n])
        for i in range((len(cur) - len(l_rule)) + 1):
            cur_ind = cur[i:i + len(l_rule)]
            if cur_ind == l_rule:
                new_cur = [] + cur
                new_cur[i:i + len(l_rule)
                        ] = list(rules[list(rules)[rule_n]])
                add_list = [rule_n + 1, i + 1, "".join(new_cur)]
                if add_list not in done[r]:
                    done[r].append(add_list)
                    return new_cur, add_list

def find_switch(times, start, end):
    r = 0
    cur = list(start)
    cur_list = []
    while r < times:
        cur, add_list = go_current_switch(cur, r)
        cur_list.append(add_list)
        r += 1
        print(done)
    return cur_list[-1][-1] == end, None
    

found = False

done = collections.defaultdict(list)

while found == False:
    found, cur_end = find_switch(times, start, end)
    print(found)
print(cur_end)
