lets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
k = int(input())

s = input()

new_s = ""

for i in range(len(s)):
    shift_pos = lets.index(s[i]) - ((3 * (i + 1)) + k)
    if shift_pos < 0:
        new_pos = len(lets) + shift_pos
        loops = new_pos // len(lets)
        shift_pos = (new_pos) - (loops * len(lets))
    new_s += lets[shift_pos]
print(new_s)