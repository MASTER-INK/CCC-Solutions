'''  Harp Tuning '''
import collections
import string
def main():
    inst = list(input())
    lets = []
    tig = collections.defaultdict(int)
    let = 0
    while let < len(inst):
        if inst[let] != "+" and inst[let] != "-":
            if inst[let] in string.ascii_uppercase:
                lets.append(inst[let])
            let += 1
        else:
            if inst[let] == "-":
                negative = True
            else:
                negative = False
            num = ""
            let += 1
            while let <= len(inst) - 1 and inst[let] in string.digits:
                num += inst[let]
                let += 1
            num = int(num)
            if negative:
                num = num * -1
            for l in lets:
                tig[l] += num
            lets = []
    last_m = inst[0]
    s = ""
    for m in tig:
        if tig[m] == tig[last_m]:
            s += m
        else:
            print(s, "tighten " + (str(tig[last_m])) if tig[last_m] > 0 else "loosen " + (str(tig[last_m] * -1)))
            s = ""
            s += m
        last_m = m
    print(s, "tighten " + str(tig[last_m]) if tig[last_m] > 0 else "loosen " + str(tig[last_m] * -1))



if __name__ == "__main__":
    main()
