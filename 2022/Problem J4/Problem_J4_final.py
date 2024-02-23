'''Problem J4/S2: Good Groups'''
import collections
def Good_groups():
    X = int(input())
    together = collections.defaultdict(list)
    for k in range(X):
        o, t = input().split()
        together[o] += [t]


    Y = int(input())
    seperate = collections.defaultdict(list)
    for l in range(Y):
        o, t = input().split()
        seperate[o] += [t]

    conflicts = 0
    def list_check(names, list, tog):
        conflicts = 0
        for m in names:
            if len(list[m]) > 0:
                for l in list[m]:
                    if tog == True:
                        if l not in names:
                            conflicts += 1
                    else:
                        if l in names:
                            conflicts += 1
        return conflicts

    G = int(input())
    for m in range(G):
        names = input().split()
        conflicts += list_check(names, together, True)
        conflicts += list_check(names, seperate, False)


    print(int(conflicts))

if __name__ == "__main__":
    Good_groups()
