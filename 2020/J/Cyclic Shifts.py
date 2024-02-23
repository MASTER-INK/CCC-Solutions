T = input()
S = input()
S += " "
def cyc(S):
    for l in range(len(S)):
        if S[l:-1] + S[0:l] in T:
            return True
    return False

print("yes" if cyc(S) else "no")
