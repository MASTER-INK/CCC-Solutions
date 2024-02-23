def main():
    N = input()
    H = input()
    def cyclic(string):
        lis = []
        for l in range(len(string)):
            lis.append(string[0:l] + string[-1] + string[l:-1])
        return lis

    p = cyclic(N)
    x = 0
    already = []
    for k in p:
        if k in H:
            if H.index(k) not in already:
                x += 1
                already.append(H.index(k))
    print(x)


if __name__ == "__main__":
    main()
