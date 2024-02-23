inst = list(input())
struct = []
while inst != ["9", "9", "9", "9", "9"]:
    struct.append(inst)
    inst = list(input())
for i in range(len(struct)):
    ins = struct[i]
    print(last + (ins[2] + ins[3] + ins[4]) if (int(ins[0]) + int(ins[1])) == 0 else "left " + (ins[2] + ins[3] + ins[4]) if (int(ins[0]) + int(ins[1])) % 2 else  "right " + (ins[2] + ins[3] + ins[4]))
    if (int(ins[0]) + int(ins[1])) != 0:
        last = "left " if (int(ins[0]) + int(ins[1])) % 2 else "right "
