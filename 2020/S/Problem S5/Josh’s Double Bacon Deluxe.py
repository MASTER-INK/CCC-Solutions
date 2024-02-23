def burger():
    N = int(input())
    bg = input().split()
    josh = int(bg[-1])
    M = int(sorted(bg)[-1])
    print(1 / M)

if __name__ == "__main__":
    burger()
