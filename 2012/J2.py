last = int(input())
bool = None
fish = "None"
def get_fish(l_1, l_2):
    if l_1 - l_2 > 0:
        bool = "Fish Rising"
    elif l_1 - l_2 < 0:
        bool = "Fish Diving"
    else:
        bool = "Fish At Constant Depth"
    return bool

for f in range(3):
    cur = int(input())
    if bool == None:
        bool = get_fish(cur, last)
    else:
        if get_fish(cur, last) != bool:
            bool = "No Fish"
    last = cur
print(bool)