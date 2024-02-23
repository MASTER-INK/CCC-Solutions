import os


def go(file_n):

    with open(file_n + ".in") as data:
        n = None
        for line in data:
                if n == None:
                    n = line.strip()
                else:
                    boards = list(map(int, line.strip().split()))

    L = [0]*2001
    F = [0]*4001

    for board in boards:
        L[int(board)] += 1

    for i in range(0, len(L) - 1):
        for j in range(i, len(L)):
            if i == j:
                F[i + j] += L[i] // 2
            else:
                F[i + j] += min(L[i], L[j])
        print(i)

    longest, size = 0, 0

    #print(list(map(lambda x: (x, F.index(x)) if x > 0 else False, F)))

    for fenceLength in F:
        if fenceLength > longest:
            longest = fenceLength
            size = 1
        elif fenceLength == longest:
            size += 1

    print(longest, size)

if __name__ == "__main__":
    os.chdir("C:\\Users\\rmath\\Visual Code\\CCC\\2017\\J\\j5")
    for k in range(1, 20):
        go("j5." + (2 - len(str(k))) * "0" + str(k))
