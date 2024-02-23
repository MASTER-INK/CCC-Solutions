def main():
    N = int(input())
    speed_data = {}

    for i in range(N):
        T, X = input().split()
        speed_data[int(T)] = int(X)

    fastest = []
    for l in range(len(sorted(speed_data)) - 1):
        dif = speed_data[sorted(speed_data)[l + 1]] - speed_data[sorted(speed_data)[l]]
        fastest.append(abs(dif) / (sorted(speed_data)[l + 1] - sorted(speed_data)[l]))

    print(sorted(fastest)[-1])


if __name__ == "__main__":
    main()
